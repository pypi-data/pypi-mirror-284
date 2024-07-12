Lazy CMS
========

Minimalistic CMS in Python with Markdown content

Features
--------

* No storages, simple file structure
* Markdown content with images
* Static auto-collection
* Simple pagination

Requirements
------------

* Python 3.12
* FastAPI 0.111.0
* Jinja2 3.1.4
* Markdown 3.6
* PyYAML 6.0.1
* python-slugify 8.0.4
* pydantic 2.8.2

Install
-------

.. code-block:: bash

    python3.12 -m venv venv
    source venv/bin/activate
    pip install lazycms

Usage
-----

Example project structure:

* project/
    * static/
        * content/ - empty directory, static content will be collected here
        * theme/ - your theme css/js
    * storage/ - your file storage directory
        * article-1/ - entity (article) directory
            * content.md - your article
            * meta.yml - entity metadata
            * picture.jpeg - picture for your article
            * preview.md - entity article miniature for index page
        * article-2/
            * content.md
            * meta.yml
            * picture.jpeg
            * preview.md
    * templates/ - Jinja2 templates directory
        * index.html - entity index template with **entity** and **paginator** context objects
        * entity.html - entity template with **entity** context object
    * app.py - CMS code
    * app.yml - CMS config

project/storage/article-1/content.md:

.. code-block:: markdown

    # Article 1

    ![Article 1]({{slug_url}}/picture.jpeg "Article 1")

    Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna
    aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat.
    Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur
    sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum.

project/storage/article-1/preview.md:

.. code-block:: markdown

    ![Article 1]({{slug_url}}/picture.jpeg "Article 1")

    # Article 1

    Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna
    aliqua. Ut enim ad minim veniam...

project/storage/article-1/meta.yml:

.. code-block:: yaml

    timestamp: !!timestamp 2024-01-01T17:00:00Z
    title: Article 1
    content: content.md
    preview: preview.md
    images:
        - picture.jpeg
    tags:
        - article
        - test

project/templates/index.html:

.. code-block:: html

    {% for entity in entities %}
        <article>
            {{ entity.preview|safe }}
        </article>
    {% endfor %}

    {% if paginator.page > 1 %}
        <a href="/?page={{ paginator.page - 1 }}">Prev</a>
    {% else %}
        Prev
    {% endif %}
    {% if paginator.page < paginator.page_count %}
        <a href="/?page={{ paginator.page + 1 }}">Next</a>
    {% else %}
        Next
    {% endif %}

project/templates/entity.html:

.. code-block:: html

    <article>
        {{ entity.content|safe }}
    </article>

project/app.yml:

.. code-block:: yaml

    # Storage config
    storage_type: FILE
    storage_path: ./storage
    storage_meta: meta.yml
    # Static config
    static_path: ./static
    static_url: /static
    # Static collected content config
    collect_path: ./static/content
    collect_url: /static/content
    # Templates
    templates_path: ./templates
    # Pagination
    paginate: 10

project/app.py:

.. code-block:: python

    from lazycms import LazyCMS


    cms = LazyCMS(config_path='app.yml')

Run:

.. code-block:: bash

    uvicorn app:cms.app --reload

http://localhost:8000 - index page

http://localhost:8000/2024-01-01-article-1 - Article 1 page

http://localhost:8000/2024-01-02-article-2 - Article 2 page

Tests
-----

TBD
