"""User repository file."""

from sqlalchemy import select
from sqlalchemy.exc import ProgrammingError
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.orm import sessionmaker, selectinload

from ..models.User import User


class UserRepo:
    session: AsyncSession

    def __init__(self, session: AsyncSession):
        self.session = session

    async def new(
            self,
            user_id: int,
            username: str | None = None,
    ) -> None:
        await self.session.merge(
            User(
                user_id=user_id,
                username=username,
            )
        )

    async def get_user(self, user_id: int) -> User:
        sql = select(User).where(User.user_id == user_id)
        result = await self.session.execute(sql)
        return result.scalars().one()

    async def is_user_exists(self, user_id: int) -> bool:
        sql = select(User.user_id).where(User.user_id == user_id)
        request = (await self.session.execute(sql)).scalars().unique().one_or_none()
        return bool(request)
