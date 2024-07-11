# <p align=center>ConfManager</p>

### Описание

<p style="font-size:14pt">Данная библиотека служит для удобного и гибкого управления конфигурациями приложения.</p>

### Примеры

<p style="font-size:14pt">Создание конфигурации</p>

```python
from simplest_conf_manager.base_config import BaseConfig
from *.brokers.broker_config
import BrokerConfig
from *.databases
import Databases


class Config(BaseConfig):
    databases: Databases
    broker: BrokerConfig
```

<p>В примере выше в качестве * используйте свои собственные валидаторы, унаследованные от BaseModel из Pydantic. Описание в файле конфигурации может выглядеть примерно так:</p>

```toml
[databases]
[databases.main]
host="localhost"
port=1234
username="username"
password="secret"
name="db_name"

[broker]
host="localhost"
port=1234
username="guest"
password="guest"
driver="driver_name"
```

<p>Можно создавать сразу несколько конфигурационных файлов различных форматов (вплоть до отдельных конфигурационных серверов). Объединяются они следующим образом:</p>

<br>
conf.toml

```toml
[connection]
host="localhost"
port=1234
username="from secrets"
password="from secrets"  # тут может быть любой текст или это может отсутствовать вовсе
```

<br>
secrets.toml

```toml
[connection]
username="username"
password="pwd"
```

<br>
config.py

```python
from simplest_conf_manager.utils.data_providers.file_data_provider import FileDataProvider
from simplest_conf_manager.utils.parsers.toml_parser import TomlParser
from simplest_conf_manager.utils.dictionaries.deep_merge import deep_merge
from simplest_conf_manager import BaseConfig
from pydantic import BaseModel


class Connection(BaseModel):
    host: str
    port: int
    username: str
    password: str


class Config(BaseConfig):
    connection: Connection


config_path = 'config/conf.toml'
secret_path = 'config/secrets.toml'

conf_provider = FileDataProvider(path=config_path)
secret_provider = FileDataProvider(path=secret_path)

conf_parser = TomlParser(conf_provider)
secret_parser = TomlParser(secret_provider)

config = Config(**deep_merge(conf_parser.parse(), secret_parser.parse()))

```

<p>Здесь следует обратить внимание на то, что при наличии одинаковых ключей в нескольких словарях (при использовании функции deep_merge) значение будет взято из последнего.</p>


<style>
p {
    font-size: 14pt;
}
</style>
