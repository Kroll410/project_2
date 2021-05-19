import pathlib
import logging

BASE_DIR = pathlib.Path(__file__).parent
SQL_DIR = pathlib.Path(__file__).parent.joinpath('sql')
LOGS_DIR = BASE_DIR.joinpath("logs").joinpath("changes.log")

with open(f'{LOGS_DIR}', 'w+') as log_file:
    logging.basicConfig(filename=f'{LOGS_DIR}', level=logging.INFO)


class Config:
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SQLALCHEMY_DATABASE_URI = 'mysql+pymysql://root:22egatob@localhost/project'
