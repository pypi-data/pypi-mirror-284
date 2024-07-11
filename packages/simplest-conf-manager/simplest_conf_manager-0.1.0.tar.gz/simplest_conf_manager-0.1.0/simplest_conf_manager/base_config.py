from abc import ABC
from functools import reduce

from pydantic import BaseModel

from simplest_conf_manager.utils.dictionaries.deep_merge import deep_merge
from simplest_conf_manager.utils.parsers.base_parser import BaseParser


class BaseConfig(BaseModel, ABC):
    @classmethod
    def read_config(cls, *parsers: tuple[BaseParser]) -> 'BaseConfig':
        dict_configs = tuple(map(lambda x: x.parse(), parsers))
        return cls(**reduce(lambda a, b: deep_merge(a, b), dict_configs))
