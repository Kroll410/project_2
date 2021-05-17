from init import db
from config import Config
import os
from config import SQL_DIR

con = db.create_engine(Config.SQLALCHEMY_DATABASE_URI, {})
meta = db.MetaData(bind=con)


def init_db():
    db.drop_all()
    db.create_all()
    for filename in [x for x in os.listdir('/home/rabb1t/PycharmProjects/project_2/sql') if x.endswith('.sql')]:
        with open(f'{SQL_DIR}/{filename}', 'r') as file:
            for query in [x.strip() for x in file.read().split('--')]:
                con.execute(query)
