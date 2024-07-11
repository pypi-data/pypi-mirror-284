from abc import ABC, abstractmethod


class BaseDataProvider(ABC):
    @abstractmethod
    def get_data(self) -> str:
        ...
