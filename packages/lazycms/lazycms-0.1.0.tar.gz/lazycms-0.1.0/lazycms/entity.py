from dataclasses import dataclass
from datetime import datetime

from pydantic import BaseModel


class MetaSchema(BaseModel):
    timestamp: datetime
    title: str
    content: str
    preview: str
    images: list[str] | None
    tags: list[str] | None


@dataclass(kw_only=True)
class Image:
    name: str
    path: str
    url: str


@dataclass(kw_only=True)
class Entity:
    timestamp: datetime
    title: str
    slug: str
    content: str
    preview: str
    images: list[Image] | None
    tags: list[str] | None
