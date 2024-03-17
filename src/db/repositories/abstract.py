"""Repository file."""
import abc
from typing import Generic, TypeVar
from collections.abc import Sequence

from sqlalchemy import delete, select
from sqlalchemy.ext.asyncio import AsyncSession

from ..models.base import Base

AbstractModel = TypeVar('AbstractModel')


class Repository(Generic[AbstractModel]):
    """Repository abstract class."""

    type_model: type[Base]
    session: AsyncSession

    def __init__(self, type_model: type[Base], session: AsyncSession):
        """Initialize abstract repository class.

        :param type_model: Which model will be used for operations
        :param session: Session in which repository will work.
        """
        self.type_model = type_model
        self.session = session
