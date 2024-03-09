import sqlalchemy as sa
import sqlalchemy.orm as orm
from sqlalchemy.orm import Mapped, mapped_column


class User:
    __tablename__ = 'Users'
    user_id: Mapped[int] = mapped_column(
        sa.BigInteger, unique=True, nullable=False
    )

    user_name: Mapped[str] = mapped_column(
        sa.Text, unique=False, nullable=True
    )