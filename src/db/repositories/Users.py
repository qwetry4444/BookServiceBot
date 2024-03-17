"""User repository file."""

from sqlalchemy import select
from sqlalchemy.exc import ProgrammingError
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.orm import sessionmaker, selectinload

from ..models.Users import Users
from .abstract import Repository


class UserRepo(Repository[Users]):
    session: AsyncSession
    type_model: type

    def __init__(self, session: AsyncSession):
        self.session = session

    async def new(
            self,
            user_id: int,
            username: str | None = None,
    ) -> None:
        await self.session.merge(
            Users(
                user_id=user_id,
                username=username,
            )
        )
        await self.session.commit()

    async def get_user(self, user_id: int) -> Users:
        sql = select(Users).where(Users.user_id == user_id)
        result = await self.session.execute(sql)
        return result.scalars().one_or_none()

    async def is_user_exists(self, user_id: int) -> bool:
        sql = select(Users.user_id).where(Users.user_id == user_id)
        request = (await self.session.scalar(sql))
        return bool(request)
