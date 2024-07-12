from dataclasses import dataclass

from fastapi import FastAPI, Request
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from fastapi.responses import HTMLResponse

from .config import Config, StorageType
from .storage import FileStorage


@dataclass(kw_only=True)
class Paginator:
    page_count: int
    page: int


class LazyCMS:
    config: Config
    storage: FileStorage
    app: FastAPI

    def __init__(self, *, config_path: str):
        self.config = Config(config_path=config_path)

        match self.config.storage_type:
            case StorageType.FILE:
                self.storage = FileStorage(config=self.config)
            case _:
                raise NotImplementedError(f'Storage {self.config.storage_type} is not implemented')

        app = FastAPI()
        app.mount(
            self.config.static_url,
            StaticFiles(directory=self.config.static_path),
            name='static',
        )
        templates = Jinja2Templates(directory=self.config.templates_path)

        @app.get('/', response_class=HTMLResponse)
        async def index(request: Request, page: int = 1):
            page_count = self.storage.count() // self.config.paginate + \
                         int(bool(self.storage.count() % self.config.paginate))
            if page < 1 or page > page_count:
                page = 1

            paginator = Paginator(page_count=page_count, page=page)
            entities = self.storage.slice(start=(page - 1) * self.config.paginate, stop=page * self.config.paginate)
            return templates.TemplateResponse(
                request=request,
                name='index.html',
                context={'paginator': paginator, 'entities': entities},
            )

        @app.get('/{slug}', response_class=HTMLResponse)
        async def entity(request: Request, slug: str):
            entity_ = self.storage.get(slug=slug)
            return templates.TemplateResponse(request=request, name='entity.html', context={'entity': entity_})

        self.app = app
