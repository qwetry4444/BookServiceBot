"""Database class with all-in-one features."""

from sqlalchemy.engine.url import URL
from sqlalchemy.ext.asyncio import AsyncEngine, AsyncSession
from sqlalchemy.ext.asyncio import create_async_engine as _create_async_engine

from .repositories import UserRepo


def create_async_engine(url: URL | str) -> AsyncEngine:
    return _create_async_engine(url=url, pool_pre_ping=True)


class Database:
    user: UserRepo

    session: AsyncSession

    def __init__(
        self,
        session: AsyncSession,
        user: UserRepo = None,
    ):
        self.session = session
        self.user = user or UserRepo(session=session)