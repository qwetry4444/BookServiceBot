"""User repository file."""

from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession

from ..models import User


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

    # async def get_role(self, user_id: int) -> Role:
    #     """Get user role by id."""
    #     return await self.session.scalar(
    #         select(User.role).where(User.user_id == user_id).limit(1)
    #     )
