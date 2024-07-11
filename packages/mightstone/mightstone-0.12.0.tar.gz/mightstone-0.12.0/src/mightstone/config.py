import json
import logging
import os
import pathlib
from enum import Enum
from typing import Literal, Optional, Tuple, Type, Union

import toml
import yaml
from pydantic.networks import MongoDsn
from pydantic_settings import (
    BaseSettings,
    InitSettingsSource,
    JsonConfigSettingsSource,
    PydanticBaseSettingsSource,
    SettingsConfigDict,
    TomlConfigSettingsSource,
    YamlConfigSettingsSource,
)
from slugify import slugify

from mightstone.core import MightstoneError

logger = logging.getLogger("mightstone")


class DbImplem(str, Enum):
    LOCAL = "local"
    MOTOR = "motor"
    FAKE = "fake"


class IjsonEnum(str, Enum):
    YAJL2_C = "yajl2_c"
    YAJL2_CFFI = "yajl2_cffi"
    YAJL2 = "yajl2"
    YAJL = "yajl"
    PYTHON = "python"


class HttpCacheSettings(BaseSettings):
    persist: bool = True
    directory: Optional[pathlib.Path] = None
    methods: list[str] = ["GET"]
    status: list[int] = [200, 203, 300, 301, 308]


class HttpSettings(BaseSettings):
    cache: HttpCacheSettings = HttpCacheSettings()


class InMemorySettings(BaseSettings):
    implementation: Literal[DbImplem.LOCAL] = DbImplem.LOCAL
    directory: Optional[pathlib.Path] = None
    database: str = "mightstone"


class MotorSettings(BaseSettings):
    implementation: Literal[DbImplem.MOTOR] = DbImplem.MOTOR
    uri: MongoDsn
    database: str = "mightstone"


class FakeSettings(BaseSettings):
    implementation: Literal[DbImplem.FAKE] = DbImplem.FAKE
    database: str = "mightstone"


class MightstoneSettings(BaseSettings):
    appname: str = "Mightstone"
    storage: Union[InMemorySettings, MotorSettings, FakeSettings] = InMemorySettings()
    http: HttpSettings = HttpSettings()
    ijson: IjsonEnum = IjsonEnum.PYTHON

    model_config = SettingsConfigDict(
        {
            "env_prefix": "mightstone_",
            "env_nested_delimiter": "__",
            "env_file_encoding": "utf-8",
        }
    )

    @classmethod
    def settings_customise_sources(
        cls,
        settings_cls: Type[BaseSettings],
        init_settings: PydanticBaseSettingsSource,
        env_settings: PydanticBaseSettingsSource,
        dotenv_settings: PydanticBaseSettingsSource,
        file_secret_settings: PydanticBaseSettingsSource,
    ) -> Tuple[PydanticBaseSettingsSource, ...]:
        return (
            init_settings,
            SettingsSourceGenerator("mightstone").build(settings_cls),
            env_settings,
            dotenv_settings,
            file_secret_settings,
        )


class SettingsSourceGenerator:
    def __init__(
        self, app_name: str = "mightstone", env_variable: Optional[str] = None
    ):
        self.app_name = slugify(app_name, separator="_")
        if not env_variable:
            env_variable = f"{self.app_name.upper()}_CONFIG_FILE"
        self.env_variable = env_variable

    def candidate_paths(
        self,
    ) -> list[pathlib.Path]:
        candidate = os.getenv(self.env_variable)
        if candidate:
            return [pathlib.Path(candidate)]

        return [
            pathlib.Path(path).joinpath(f"{self.app_name}.{extension}")
            for path in [os.getcwd(), os.path.expanduser("~")]
            for extension in ["yaml", "yml", "json", "toml"]
        ]

    @classmethod
    def load_file(cls, filepath, encoding):
        try:
            with open(filepath, "r", encoding=encoding) as f:
                _, extension = os.path.splitext(filepath)
                if extension.lower() in [".yml", ".yaml"]:
                    return yaml.safe_load(f)

                if extension.lower() == ".toml":
                    return toml.load(f)

                return json.load(f)
        except Exception as e:
            raise MightstoneError("Unable to parse %s" % filepath) from e

    def build(self, settings_cls: Type[BaseSettings]) -> Union[
        InitSettingsSource,
        JsonConfigSettingsSource,
        YamlConfigSettingsSource,
        TomlConfigSettingsSource,
    ]:
        for candidate in self.candidate_paths():
            if not candidate.exists():
                continue

            _, extension = os.path.splitext(candidate)
            try:
                if extension.lower() in [".yml", ".yaml"]:
                    return YamlConfigSettingsSource(settings_cls, candidate)

                if extension.lower() == ".toml":
                    return TomlConfigSettingsSource(settings_cls, candidate)

                return JsonConfigSettingsSource(settings_cls, candidate)
            except MightstoneError as e:
                logger.fatal("Unable to parse configuration from %s, %s", candidate, e)

        return InitSettingsSource(settings_cls, {})
