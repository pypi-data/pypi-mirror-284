from datetime import datetime

from jinja2 import Environment, BaseLoader
from markdown import markdown
from slugify import slugify as slugify_


def slugify(*, timestamp: datetime, title: str) -> str:
    return f'{timestamp.strftime("%Y-%m-%d")}-{slugify_(title)}'


def render(*, md_path: str, collect_url: str, slug: str) -> str:
    with open(md_path, 'r') as fp:
        data = fp.read()
    md = markdown(data, extensions=['attr_list'])
    template = Environment(loader=BaseLoader()).from_string(md)
    return template.render(slug_url=f'{collect_url}/{slug}')
