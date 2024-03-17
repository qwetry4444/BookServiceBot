import sqlalchemy as sa
import sqlalchemy.orm as orm
from sqlalchemy.orm import Mapped, mapped_column

from .base import Base


class Users(Base):
    __tablename__ = 'Users'
    user_id: Mapped[int] = mapped_column(
        sa.BigInteger, unique=True, nullable=False, primary_key=True
    )

    username: Mapped[str] = mapped_column(
        sa.Text, unique=False, nullable=True
    )
