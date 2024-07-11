from abc import ABC, abstractmethod
from typing import Type, Optional

from simplest_conf_manager.utils.data_providers.base_data_provider import BaseDataProvider


class BaseParser(ABC):  # type: ignore
    def __init__(self,
                 payload: Optional[str | BaseDataProvider] = None):
        self.payload = payload

    def parse(self,
              payload: Optional[str | BaseDataProvider] = None) -> dict:
        if payload is None:
            payload = self.payload

        if isinstance(payload, BaseDataProvider):
            payload: str = payload.get_data()

        return self._parse(payload)

    @abstractmethod
    def _parse(self, payload: str) -> dict:
        ...
