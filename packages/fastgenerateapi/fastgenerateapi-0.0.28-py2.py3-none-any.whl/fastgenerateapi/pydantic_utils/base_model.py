import importlib
from typing import List

from pydantic import BaseModel as PydanticBaseModel, Extra, BaseConfig

from fastgenerateapi.pydantic_utils.json_encoders import JSON_ENCODERS
from fastgenerateapi.settings.register_settings import settings

try:
    module_path, class_name = settings.app_settings.ALIAS_GENERATOR.rsplit('.', maxsplit=1)
    module = importlib.import_module(module_path)
    alias_generator = getattr(module, class_name)
except Exception:
    alias_generator = None


class Config(BaseConfig):
    json_encoders = JSON_ENCODERS
    extra = Extra.ignore
    orm_mode = True  # v1 版本
    from_attributes = True  # v2 版本
    allow_population_by_field_name = True  # v1 版本
    populate_by_name = True  # v2 版本
    alias_generator = alias_generator


class BaseModel(PydanticBaseModel):
    class Config(Config):
        ...


class QueryConfig(Config):
    ...


class IDList(BaseModel):
    id_list: List[str] = []

    # class Config:
    #     json_encoders = JSON_ENCODERS
    #     extra = Extra.ignore
