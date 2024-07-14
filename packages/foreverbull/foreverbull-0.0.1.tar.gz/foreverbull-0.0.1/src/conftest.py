import os
import tempfile
from datetime import datetime, timedelta, timezone
from functools import partial
from multiprocessing import get_start_method, set_start_method
from threading import Thread

import pynng
import pytest
import yfinance
from sqlalchemy import Column, DateTime, Integer, String, UniqueConstraint, create_engine, engine, text
from sqlalchemy.orm import declarative_base
from testcontainers.core.container import DockerContainer
from testcontainers.core.network import Network
from testcontainers.core.waiting_utils import wait_for_logs
from testcontainers.minio import MinioContainer
from testcontainers.nats import NatsContainer
from testcontainers.postgres import PostgresContainer

from foreverbull import Order, entity, socket


@pytest.fixture(scope="session")
def spawn_process():
    method = get_start_method()
    if method != "spawn":
        set_start_method("spawn", force=True)


@pytest.fixture(scope="function")
def execution(database):
    return entity.backtest.Execution(
        id="test",
        calendar="NYSE",
        start=datetime(2023, 1, 1, 0, 0, 0, 0, tzinfo=timezone.utc),
        end=datetime(2023, 3, 31, 0, 0, 0, 0, tzinfo=timezone.utc),
        symbols=["AAPL", "MSFT", "TSLA"],
        benchmark="AAPL",
    )


@pytest.fixture(scope="function")
def namespace_server():
    namespace = dict()

    s = pynng.Rep0(listen="tcp://0.0.0.0:7878")
    s.recv_timeout = 500
    s.send_timeout = 500
    os.environ["NAMESPACE_PORT"] = "7878"

    def runner(s, namespace):
        while True:
            try:
                message = s.recv()
            except pynng.exceptions.Timeout:
                continue
            except pynng.exceptions.Closed:
                break
            request = socket.Request.deserialize(message)
            if request.task.startswith("get:"):
                key = request.task[4:]
                response = socket.Response(task=request.task, data=namespace.get(key))
                s.send(response.serialize())
            elif request.task.startswith("set:"):
                key = request.task[4:]
                namespace[key] = request.data
                response = socket.Response(task=request.task)
                s.send(response.serialize())
            else:
                response = socket.Response(task=request.task, error="Invalid task")
                s.send(response.serialize())

    thread = Thread(target=runner, args=(s, namespace))
    thread.start()

    yield namespace

    s.close()
    thread.join()


@pytest.fixture(scope="function")
def parallel_algo_file(spawn_process, execution, database):
    def _process_symbols(server_socket: pynng.Socket) -> list[Order]:
        start = execution.start
        portfolio = entity.finance.Portfolio(
            cash=0,
            value=0,
            positions=[],
        )
        orders: list[Order] = []
        while start < execution.end:
            for symbol in execution.symbols:
                req = entity.service.Request(
                    timestamp=start,
                    symbols=[symbol],
                    portfolio=portfolio,
                )
                server_socket.send(socket.Request(task="parallel_algo", data=req).serialize())
                response = socket.Response.deserialize(server_socket.recv())
                assert response.task == "parallel_algo"
                assert response.error is None
                assert response.data
                for order in response.data:
                    orders.append(Order(**order))
            start += timedelta(days=1)
        return orders

    instance = entity.service.Instance(
        id="test",
        broker_port=5656,
        database_url=os.environ["DATABASE_URL"],
        functions={"parallel_algo": entity.service.Instance.Parameter(parameters={})},
    )

    process_socket = pynng.Req0(listen="tcp://127.0.0.1:5656")
    process_socket.recv_timeout = 5000
    process_socket.send_timeout = 5000
    _process_symbols = partial(_process_symbols, server_socket=process_socket)

    with tempfile.NamedTemporaryFile(suffix=".py") as f:
        f.write(
            b"""
from random import choice
from foreverbull import Algorithm, Function, Portfolio, Order, Asset

def parallel_algo(asset: Asset, portfolio: Portfolio) -> Order:
    return choice([Order(symbol=asset.symbol, amount=10), Order(symbol=asset.symbol, amount=-10)])

Algorithm(
    functions=[
        Function(callable=parallel_algo)
    ]
)
"""
        )
        f.flush()

        yield f.name, instance, _process_symbols
        process_socket.close()


@pytest.fixture(scope="function")
def non_parallel_algo_file(spawn_process, execution, database):
    def _process_symbols(server_socket: pynng.Socket) -> list[Order]:
        start = execution.start
        portfolio = entity.finance.Portfolio(
            cash=0,
            value=0,
            positions=[],
        )
        orders: list[Order] = []
        while start < execution.end:
            req = entity.service.Request(
                timestamp=start,
                symbols=execution.symbols,
                portfolio=portfolio,
            )
            server_socket.send(socket.Request(task="non_parallel_algo", data=req).serialize())
            response = socket.Response.deserialize(server_socket.recv())
            assert response.task == "non_parallel_algo"
            assert response.error is None
            assert response.data
            for order in response.data:
                orders.append(Order(**order))

            start += timedelta(days=1)
        return orders

    instance = entity.service.Instance(
        id="test",
        broker_port=5657,
        database_url=os.environ["DATABASE_URL"],
        functions={
            "non_parallel_algo": entity.service.Instance.Parameter(
                parameters={},
            )
        },
    )

    process_socket = pynng.Req0(listen="tcp://127.0.0.1:5657")
    process_socket.recv_timeout = 5000
    process_socket.send_timeout = 5000
    _process_symbols = partial(_process_symbols, server_socket=process_socket)

    with tempfile.NamedTemporaryFile(suffix=".py") as f:
        f.write(
            b"""
from random import choice
from foreverbull import Algorithm, Function, Portfolio, Order, Assets

def non_parallel_algo(assets: Assets, portfolio: Portfolio) -> list[Order]:
    orders = []
    for asset in assets:
        orders.append(choice([Order(symbol=asset.symbol, amount=10), Order(symbol=asset.symbol, amount=-10)]))
    return orders

Algorithm(
    functions=[
        Function(callable=non_parallel_algo)
    ]
)
"""
        )
        f.flush()
        yield f.name, instance, _process_symbols
        process_socket.close()


@pytest.fixture(scope="function")
def parallel_algo_file_with_parameters(spawn_process, execution, database):
    def _process_symbols(server_socket) -> list[Order]:
        start = execution.start
        portfolio = entity.finance.Portfolio(
            cash=0,
            value=0,
            positions=[],
        )
        orders: list[Order] = []
        while start < execution.end:
            for symbol in execution.symbols:
                req = entity.service.Request(
                    timestamp=start,
                    symbols=[symbol],
                    portfolio=portfolio,
                )
                server_socket.send(socket.Request(task="parallel_algo_with_parameters", data=req).serialize())
                response = socket.Response.deserialize(server_socket.recv())
                assert response.task == "parallel_algo_with_parameters"
                assert response.error is None
                assert response.data
                for order in response.data:
                    orders.append(Order(**order))

            start += timedelta(days=1)
        return orders

    instance = entity.service.Instance(
        id="test",
        broker_port=5658,
        database_url=os.environ["DATABASE_URL"],
        functions={
            "parallel_algo_with_parameters": entity.service.Instance.Parameter(
                parameters={
                    "low": "15",
                    "high": "25",
                }
            )
        },
    )

    process_socket = pynng.Req0(listen="tcp://127.0.0.1:5658")
    process_socket.recv_timeout = 5000
    process_socket.send_timeout = 5000
    _process_symbols = partial(_process_symbols, server_socket=process_socket)

    with tempfile.NamedTemporaryFile(suffix=".py") as f:
        f.write(
            b"""
from random import choice
from foreverbull import Algorithm, Function, Portfolio, Order, Asset

def parallel_algo_with_parameters(asset: Asset, portfolio: Portfolio, low: int, high: int) -> Order:
    return choice([Order(symbol=asset.symbol, amount=10), Order(symbol=asset.symbol, amount=-10)])

Algorithm(
    functions=[
        Function(callable=parallel_algo_with_parameters)
    ]
)
"""
        )
        f.flush()
        yield f.name, instance, _process_symbols
        process_socket.close()


@pytest.fixture(scope="function")
def non_parallel_algo_file_with_parameters(spawn_process, execution, database):
    def _process_symbols(server_socket) -> list[Order]:
        start = execution.start
        portfolio = entity.finance.Portfolio(
            cash=0,
            value=0,
            positions=[],
        )
        orders: list[Order] = []
        while start < execution.end:
            req = entity.service.Request(
                timestamp=start,
                symbols=execution.symbols,
                portfolio=portfolio,
            )
            server_socket.send(socket.Request(task="non_parallel_algo_with_parameters", data=req).serialize())
            response = socket.Response.deserialize(server_socket.recv())
            assert response.task == "non_parallel_algo_with_parameters"
            assert response.error is None
            assert response.data
            for order in response.data:
                orders.append(Order(**order))
            start += timedelta(days=1)
        return orders

    instance = entity.service.Instance(
        id="test",
        broker_port=5659,
        database_url=os.environ["DATABASE_URL"],
        functions={
            "non_parallel_algo_with_parameters": entity.service.Instance.Parameter(
                parameters={
                    "low": "15",
                    "high": "25",
                },
            )
        },
    )

    process_socket = pynng.Req0(listen="tcp://127.0.0.1:5659")
    process_socket.recv_timeout = 5000
    process_socket.send_timeout = 5000
    _process_symbols = partial(_process_symbols, server_socket=process_socket)

    with tempfile.NamedTemporaryFile(suffix=".py") as f:
        f.write(
            b"""
from random import choice
from foreverbull import Algorithm, Function, Portfolio, Order, Assets

def non_parallel_algo_with_parameters(assets: Assets, portfolio: Portfolio, low: int, high: int) -> list[Order]:
    orders = []
    for asset in assets:
        orders.append(choice([Order(symbol=asset.symbol, amount=10), Order(symbol=asset.symbol, amount=-10)]))
    return orders

Algorithm(
    functions=[
        Function(callable=non_parallel_algo_with_parameters)
    ]
)
"""
        )
        f.flush()
        yield f.name, instance, _process_symbols
        process_socket.close()


@pytest.fixture(scope="function")
def multistep_algo_with_namespace(spawn_process, execution, database, namespace_server):
    def _process_symbols(server_socket) -> list[Order]:
        start = execution.start
        portfolio = entity.finance.Portfolio(
            cash=0,
            value=0,
            positions=[],
        )
        orders: list[Order] = []
        while start < execution.end:
            # filter assets
            req = entity.service.Request(
                timestamp=start,
                symbols=execution.symbols,
                portfolio=portfolio,
            )
            server_socket.send(socket.Request(task="filter_assets", data=req).serialize())
            response = socket.Response.deserialize(server_socket.recv())
            assert response.task == "filter_assets"
            assert response.error is None

            # measure assets
            for symbol in execution.symbols:
                req = entity.service.Request(
                    timestamp=start,
                    symbols=[symbol],
                    portfolio=portfolio,
                )
                server_socket.send(socket.Request(task="measure_assets", data=req).serialize())
                response = socket.Response.deserialize(server_socket.recv())
                assert response.task == "measure_assets"
                assert response.error is None

            # create orders
            req = entity.service.Request(
                timestamp=start,
                symbols=execution.symbols,
                portfolio=portfolio,
            )
            server_socket.send(socket.Request(task="create_orders", data=req).serialize())
            response = socket.Response.deserialize(server_socket.recv())
            assert response.task == "create_orders"
            assert response.error is None
            start += timedelta(days=1)
        return orders

    instance = entity.service.Instance(
        id="test",
        broker_port=5660,
        database_url=os.environ["DATABASE_URL"],
        functions={
            "filter_assets": entity.service.Instance.Parameter(
                parameters={},
            ),
            "measure_assets": entity.service.Instance.Parameter(
                parameters={
                    "low": "5",
                    "high": "10",
                },
            ),
            "create_orders": entity.service.Instance.Parameter(
                parameters={},
            ),
        },
    )

    process_socket = pynng.Req0(listen="tcp://127.0.0.1:5660")
    process_socket.recv_timeout = 5000
    process_socket.send_timeout = 5000
    _process_symbols = partial(_process_symbols, server_socket=process_socket)

    with tempfile.NamedTemporaryFile(suffix=".py") as f:
        f.write(
            b"""
from foreverbull import Algorithm, Function, Asset, Assets, Portfolio, Order, Namespace


def measure_assets(asset: Asset, portfolio: Portfolio, low: int = 5, high: int = 10) -> None:
    pass

def create_orders(assets: Assets, portfolio: Portfolio) -> list[Order]:
    pass

def filter_assets(assets: Assets, portfolio: Portfolio) -> None:
    pass

Algorithm(
    functions=[
        Function(callable=measure_assets),
        Function(callable=create_orders, run_last=True),
        Function(callable=filter_assets, run_first=True),
    ],
    namespace={"qualified_symbols": list[str], "asset_metrics": dict[str, float]}
)
"""
        )
        f.flush()
        yield f.name, instance, _process_symbols
        process_socket.close()


Base = declarative_base()


class Asset(Base):
    __tablename__ = "asset"
    symbol = Column("symbol", String(), primary_key=True)
    name = Column("name", String())
    title = Column("title", String())
    asset_type = Column("asset_type", String())


class OHLC(Base):
    __tablename__ = "ohlc"
    id = Column(Integer, primary_key=True)
    symbol = Column(String())
    open = Column(Integer())
    high = Column(Integer())
    low = Column(Integer())
    close = Column(Integer())
    volume = Column(Integer())
    time = Column(DateTime())

    __table_args__ = (UniqueConstraint("symbol", "time", name="symbol_time_uc"),)


@pytest.fixture(scope="session")
def backtest_entity():
    return entity.backtest.Backtest(
        name="testing_backtest",
        calendar="NYSE",
        start=datetime(2022, 1, 3, tzinfo=timezone.utc),
        end=datetime(2023, 12, 29, tzinfo=timezone.utc),
        symbols=[
            "AAPL",
            "AMZN",
            "BAC",
            "BRK-B",
            "CMCSA",
            "CSCO",
            "DIS",
            "GOOG",
            "GOOGL",
            "HD",
            "INTC",
            "JNJ",
            "JPM",
            "KO",
            "MA",
            "META",
            "MRK",
            "MSFT",
            "PEP",
            "PG",
            "TSLA",
            "UNH",
            "V",
            "VZ",
            "WMT",
        ],
    )


@pytest.fixture(scope="session")
def verify_database():
    def _(database: engine.Engine, backtest: entity.backtest.Backtest):
        with database.connect() as conn:
            for symbol in backtest.symbols:
                result = conn.execute(
                    text("SELECT min(time), max(time) FROM ohlc WHERE symbol = :symbol"),
                    {"symbol": symbol},
                )
                res = result.fetchone()
                if res is None:
                    return False
                start, end = res
                if start is None or end is None:
                    return False
                if start.date() != backtest.start.date() or end.date() != backtest.end.date():
                    return False
            return True

    return _


@pytest.fixture(scope="session")
def populate_database():
    def _(database: engine.Engine, backtest: entity.backtest.Backtest):
        with database.connect() as conn:
            for symbol in backtest.symbols:
                feed = yfinance.Ticker(symbol)
                info = feed.info
                asset = entity.finance.Asset(
                    symbol=info["symbol"],
                    name=info["longName"],
                    title=info["shortName"],
                    asset_type=info["quoteType"],
                )
                conn.execute(
                    text(
                        """INSERT INTO asset (symbol, name, title, asset_type)
                        VALUES (:symbol, :name, :title, :asset_type) ON CONFLICT DO NOTHING"""
                    ),
                    {"symbol": asset.symbol, "name": asset.name, "title": asset.title, "asset_type": asset.asset_type},
                )
                data = feed.history(start=backtest.start, end=backtest.end + timedelta(days=1))
                for idx, row in data.iterrows():
                    time = datetime(idx.year, idx.month, idx.day, idx.hour, idx.minute, idx.second)
                    ohlc = entity.finance.OHLC(
                        symbol=symbol,
                        open=row.Open,
                        high=row.High,
                        low=row.Low,
                        close=row.Close,
                        volume=row.Volume,
                        time=time,
                    )
                    conn.execute(
                        text(
                            """INSERT INTO ohlc (symbol, open, high, low, close, volume, time)
                            VALUES (:symbol, :open, :high, :low, :close, :volume, :time) ON CONFLICT DO NOTHING"""
                        ),
                        {
                            "symbol": ohlc.symbol,
                            "open": ohlc.open,
                            "high": ohlc.high,
                            "low": ohlc.low,
                            "close": ohlc.close,
                            "volume": ohlc.volume,
                            "time": ohlc.time,
                        },
                    )
            conn.commit()

    return _


@pytest.fixture(scope="session")
def database(backtest_entity: entity.backtest.Backtest, verify_database, populate_database):
    with PostgresContainer("postgres:alpine") as postgres:
        engine = create_engine(postgres.get_connection_url())
        Base.metadata.create_all(engine)
        os.environ["DATABASE_URL"] = postgres.get_connection_url()
        if not verify_database(engine, backtest_entity):
            populate_database(engine, backtest_entity)
        yield engine


@pytest.fixture(scope="session")
def local_environment(network, minio, nats, postgres):
    with Network() as network:
        postgres = PostgresContainer(
            "postgres:13.3-alpine",
            network=network.name,
            hostname="postgres",
            username="postgres",
            password="postgres",
            dbname="postgres",
        )
        minio = MinioContainer("minio/minio:latest", network=network.name, hostname="minio")
        nats = NatsContainer("nats:2.10-alpine", network=network.name, hostname="nats")
        nats = nats.with_command("-js")
        with postgres as postgres, minio as minio, nats as nats:
            foreverbull = DockerContainer(os.environ.get("BROKER_IMAGE", ""))
            foreverbull.with_network(network)
            foreverbull.with_env("POSTGRES_URL", "postgres://postgres:postgres@postgres:5432/postgres")
            foreverbull.with_env("NATS_URL", "nats://nats:4222")
            foreverbull.with_env("MINIO_URL", "minio:9000")
            foreverbull.with_env("BACKTEST_IMAGE", os.environ.get("BACKTEST_IMAGE", "lhjnilsson/zipline:latest"))
            foreverbull.with_volume_mapping("/var/run/docker.sock", "/var/run/docker.sock", mode="rw")
            with foreverbull as foreverbull:
                wait_for_logs(foreverbull, "RUNNING", 10)
                yield foreverbull
