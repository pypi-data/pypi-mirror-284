from setuptools import setup, find_packages

setup(
    name="bb-database",
    version="v0.0.1",
    packages=find_packages(),
    install_requires=[
        "alembic",
        "greenlet",
        "Mako",
        "MarkupSafe",
        "psycopg2",
        "python-dotenv",
        "SQLAlchemy",
        "typing_extensions",

    ],
    author="Shounak Joshi",
    author_email="sticktbit.shounak@gmail.com",
    url="https://github.com/buildingblocksInno/bb-database"
)
