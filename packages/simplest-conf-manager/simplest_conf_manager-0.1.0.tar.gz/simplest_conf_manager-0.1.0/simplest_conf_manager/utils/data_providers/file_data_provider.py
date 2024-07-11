from simplest_conf_manager.utils.data_providers.base_data_provider import BaseDataProvider


class FileDataProvider(BaseDataProvider):
    def __init__(self, path: str, modifier: str = 'r', encoding: str = 'utf-8'):
        self.path = path
        self.modifier = modifier
        self.encoding = encoding

    def get_data(self) -> str:
        with open(self.path, self.modifier, encoding=self.encoding) as f:
            return f.read()
