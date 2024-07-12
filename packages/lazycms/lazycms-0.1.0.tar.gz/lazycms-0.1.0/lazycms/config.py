from enum import StrEnum

import yaml
from pydantic import BaseModel


class StorageType(StrEnum):
    FILE: str = 'FILE'


class ConfigSchema(BaseModel):
    storage_type: StorageType
    storage_path: str
    storage_meta: str

    static_path: str
    static_url: str

    collect_path: str
    collect_url: str

    templates_path: str

    paginate: int


class Config:
    storage_type: StorageType
    storage_path: str
    storage_meta: str

    static_path: str
    static_url: str

    collect_path: str
    collect_url: str

    templates_path: str

    paginate: int

    def __init__(self, *, config_path: str):
        with open(config_path, 'r') as fp:
            data = yaml.load(fp, yaml.Loader)
        config = ConfigSchema(**data)
        for key, value in dict(config).items():
            setattr(self, key, value)
