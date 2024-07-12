import os
import shutil

import yaml

from .config import Config
from .entity import MetaSchema, Entity, Image
from .utils import slugify, render


class FileStorage:
    entities: list[Entity]
    slug_index: dict[str, Entity]

    def __init__(self, *, config: Config):
        meta_paths = [f'{config.storage_path}/{d}' for d in os.listdir(config.storage_path) if not os.path.isfile(d)]
        self.entities = []
        for meta_path in meta_paths:
            with open(f'{meta_path}/{config.storage_meta}', 'r') as fp:
                data = yaml.load(fp, yaml.Loader)
            meta = MetaSchema(**data)
            slug = slugify(timestamp=meta.timestamp, title=meta.title)
            content = render(md_path=f'{meta_path}/{meta.content}', collect_url=config.collect_url, slug=slug)
            preview = render(md_path=f'{meta_path}/{meta.preview}', collect_url=config.collect_url, slug=slug)
            images = [
                Image(name=name, path=f'{meta_path}/{name}', url=f'{config.collect_url}/{slug}/{name}')
                for name in meta.images
            ]
            entity = Entity(
                timestamp=meta.timestamp,
                title=meta.title,
                slug=slug,
                content=content,
                preview=preview,
                images=images,
                tags=meta.tags,
            )
            self.entities.append(entity)

        try:
            shutil.rmtree(config.collect_path)
        except FileNotFoundError:
            pass
        os.mkdir(config.collect_path)

        for entity in self.entities:
            if entity.images:
                os.mkdir(f'{config.collect_path}/{entity.slug}')
            for image in entity.images:
                shutil.copy2(image.path, f'{config.collect_path}/{entity.slug}/{image.name}')

        self.entities = sorted(self.entities, key=lambda e: e.timestamp, reverse=True)
        self.slug_index = {}
        for entity in self.entities:
            self.slug_index[entity.slug] = entity

    def count(self) -> int:
        return len(self.entities)

    def slice(self, *, start: int, stop: int) -> list[Entity]:
        return self.entities[start:stop]

    def get(self, *, slug: str) -> Entity | None:
        return self.slug_index.get(slug)
