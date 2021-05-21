"""
Module config.py consists of configuration set ups for logging and SQLAlchemy package
"""

import pathlib
import logging

BASE_DIR = pathlib.Path(__file__).parent
SQL_DIR = pathlib.Path(__file__).parent.joinpath('sql')
LOGS_DIR = BASE_DIR.joinpath("logs").joinpath("changes.log")

with open(f'{LOGS_DIR}', 'w+') as log_file:
    logging.basicConfig(filename=f'{LOGS_DIR}', level=logging.INFO)


class Config:
    from os import environ
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    # SQLALCHEMY_DATABASE_URI = 'postgresql+pg8000://test:12345@localhost/project'
    SQLALCHEMY_DATABASE_URI = environ.get("DATABASE_URL")