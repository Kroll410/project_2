"""
Module init_models.py consist of function to populate database with sample data
"""

import sqlalchemy.exc

from init import db
from config import Config
import os
from config import SQL_DIR
from logging import info, error
con = db.create_engine(Config.SQLALCHEMY_DATABASE_URI, {})
meta = db.MetaData(bind=con)


def init_db():
    """
    Function performs reading .sql file and executing SQL code
        that populates data to database
    :return:
    """
    db.drop_all()
    info('Dropped all presented tables in database')
    db.create_all()
    info(f'Created tables: {", ".join(x for x in con.table_names())}')
    for filename in [x for x in os.listdir('/home/rabb1t/PycharmProjects/project_2/sql') if x.endswith('.sql')]:
        with open(f'{SQL_DIR}/{filename}', 'r') as file:
            for query in [x.strip() for x in file.read().split('--')]:
                try:
                    con.execute(query)
                    info(f'Query executed: {query}')
                except sqlalchemy.exc.ProgrammingError:
                    error('SQL code has not been executed')
