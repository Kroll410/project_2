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
    from os import getenv
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    # SQLALCHEMY_DATABASE_URI = 'postgresql+pg8000://test:12345@localhost/project'
    SQLALCHEMY_DATABASE_URI = getenv("DATABASE_URL")
    if SQLALCHEMY_DATABASE_URI.startswith("postgres://"):
        SQLALCHEMY_DATABASE_URI = SQLALCHEMY_DATABASE_URI.replace("postgres://", "postgres://pbxnwtrzglyhug:9a2dfd04fb09d5ef460ff222ac791079acc438ba00496be10d421c7d797c65b1@ec2-52-50-171-4.eu-west-1.compute.amazonaws.com:5432/d4ol145u7ksscg", 1)