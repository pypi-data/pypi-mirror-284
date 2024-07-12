from setuptools import setup
from codecs import open
from os import path


here = path.abspath(path.dirname(__file__))

with open(path.join(here, 'README.rst'), encoding='utf-8') as f:
    long_description = f.read()

setup(
    name='lazycms',
    version='0.1.0',
    description='Minimalistic CMS in Python with Markdown content',
    long_description=long_description,
    url='https://github.com/neurophant/lazycms/',
    author='Anton Smolin',
    author_email='smolin.anton@gmail.com',
    license='MIT',
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Environment :: Console',
        'Framework :: FastAPI',
        'Intended Audience :: Developers',
        'Intended Audience :: Information Technology',
        'Intended Audience :: Other Audience',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 3.12',
        'Topic :: Internet :: WWW/HTTP :: Dynamic Content :: Content Management System',
        'Topic :: Software Development :: Libraries',
        'Topic :: Text Processing :: Markup :: Markdown',
    ],
    keywords='markdown cms minimalistic',
    packages=['lazycms'],
    install_requires=[
        'fastapi>=0.111.0,<1.0.0',
        'Jinja2>=3.1.4,<4.0.0',
        'Markdown>=3.6,<4.0',
        'PyYAML>=6.0.1,<7.0.0',
        'python-slugify>=8.0.4,<9.0.0',
        'pydantic>=2.8.2,<3.0.0',
    ]
)
