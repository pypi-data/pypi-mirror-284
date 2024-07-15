from abc import ABC, abstractmethod
from typing import Generic

from gptdb.component import BaseComponent
from gptdb.serve.core.config import BaseServeConfig
from gptdb.storage.metadata._base_dao import REQ, RES, BaseDao, T


class BaseService(BaseComponent, Generic[T, REQ, RES], ABC):
    name = "gptdb_serve_base_service"

    def __init__(self, system_app):
        super().__init__(system_app)

    @property
    @abstractmethod
    def dao(self) -> BaseDao[T, REQ, RES]:
        """Returns the internal DAO."""

    @property
    @abstractmethod
    def config(self) -> BaseServeConfig:
        """Returns the internal ServeConfig."""

    def create(self, request: REQ) -> RES:
        """Create a new entity

        Args:
            request (REQ): The request

        Returns:
            RES: The response
        """
        return self.dao.create(request)
