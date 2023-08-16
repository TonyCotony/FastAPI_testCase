import redis
from sqlalchemy.ext.asyncio import create_async_engine, AsyncSession
from sqlalchemy.orm import sessionmaker, declarative_base

from core.loggs.logger import logger
from settings import settings

sqlalchemy_url = f"mysql+asyncmy://{settings.db.mysql_user}@{settings.db.mysql_host}/{settings.db.mysql_db}"
engine = create_async_engine(
    url=sqlalchemy_url,
    future=True,
    echo=True, pool_pre_ping=True
)

async_session = sessionmaker(engine, class_=AsyncSession, expire_on_commit=False)

Base = declarative_base()


async def get_db():
    """db session for FastAPI depends"""
    db = async_session()
    logger.debug('Depends db session opened')
    try:
        yield db
    finally:
        await db.close()


async def get_db_session() -> AsyncSession:
    """get DB session without FastAPI Depends"""
    async with async_session() as db_session:
        logger.debug('db session opened')
        return db_session


def get_redis_connection():
    """для redis соединения"""
    return redis.Redis(
        host=settings.db.redis_host,
        port=settings.db.redis_port
    )
