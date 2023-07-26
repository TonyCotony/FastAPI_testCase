import redis
from sqlalchemy.ext.asyncio import create_async_engine, AsyncSession
from sqlalchemy.orm import sessionmaker, declarative_base

sqlalchemy_url = "mysql+asyncmy:///root:12345@localhost/cargo_db"
engine = create_async_engine(
    url=sqlalchemy_url,
    future=True,
    echo=True, pool_pre_ping=True
)

Async_session = sessionmaker(engine, class_=AsyncSession, expire_on_commit=False)

Base = declarative_base()


async def get_db():
    db = Async_session()
    try:
        yield db
    finally:
        await db.close()

redis_uri = 'redis://localhost:6379/0'

redis_connection = redis.StrictRedis(
    host=redis_uri,
    charset="utf-8",
    decode_responses=True
)
