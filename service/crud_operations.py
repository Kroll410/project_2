"""
Module crud_operations consists of functions which perform CRUD operation upon database
"""

import config
from init import db
from models.models import MODELS
from helpers.validation import VALIDATE

from logging import info, error

con = db.create_engine(config.Config.SQLALCHEMY_DATABASE_URI, {})
meta = db.MetaData(bind=con)


def select_from_table(table_name, id=None, show_all=False):
    """
    Function performs select operation on table
    :param table_name: name of the table to retrieve data
    :param id: optional value, used to retrieve data from specific row by id
    :param show_all: If True, retrieve all row data otherwise retrieve only basic information
    :return: list of dictionaries with data if id=True, else dictionary with data
    """
    if id is None:
        table = db.session.query(MODELS[str(table_name).capitalize()]).all()
        return [el.get_info_dict() for el in table] if show_all else [el.to_dict() for el in table]

    row = db.session.query(MODELS[str(table_name).capitalize()]).filter_by(id=id).first()
    if not row:
        return {}

    return row.get_info_dict() if show_all else row.to_dict()


def get_all_tables_col_info() -> dict:
    """
    Function get all tables column names from models
    :return: list of dictionaries [{table_name: [column_name_1, ...], ... }]
    """
    inspector = db.inspect(con)
    tables = inspector.get_table_names()

    data = {}
    for table in tables:
        data.update({table: []})
        for column in inspector.get_columns(table):
            data[table].append(column['name'])

    return data


def get_table_relations_data(table_name):
    """
    Function finds relation field between specific table and values and returns them
    :param table_name: specific table name
    :return: {table_name: {col_name: [values], ... }, ...}
    """
    relation_data = MODELS[table_name].get_relations(MODELS[table_name])
    table_relations = {}

    for idx, pair in enumerate(relation_data.items()):

        t_name = pair[0]
        curr_table_relations = {}

        for field in pair[1]:
            if field == 'id':
                curr_table_relations.update({
                    'id': [x + 1 for x in range(len(select_from_table(t_name)))]
                })

        table_relations.update({
            t_name: curr_table_relations
        })

    if table_name == 'Orders':
        for row in select_from_table(table_name, show_all=True):
            if (_id := row['platform_id']) in table_relations['Platforms']['id']:
                table_relations['Platforms']['id'].remove(_id)

    return table_relations


def get_table_fields_data(table_name):
    """
    Function returns basic data from table
    :param table_name: name of specific table
    :return: {col_name: [values], ...}
    """
    table = MODELS[table_name]
    return table.to_dict(table).keys()


def get_table_info_fields_data(table_name):
    """
    Function returns all data from table
    :param table_name: name of specific table
    :return: {col_name: [values], ...}
    """
    table = MODELS[table_name]
    return table.get_info_dict(table).keys()


def check_unique_data_presence(table_name, data):
    """
    Function checks data presence for unique constraint columns in table
    :param table_name: name of specific table
    :param data: data to be checked with already presented
    :param row_id: optional. Used to check data uniqueness with on specific row
    :return: True if data is already exists False otherwise
    """
    table = MODELS[table_name]

    for row in select_from_table(table_name):
        for column_name, value in row.items():
            c = table.__table__.columns.get(column_name)
            if c.unique and data[column_name] == value:
                return True

    return False


def insert_into_table(table_name, data, id=None):
    """
    Function perform insertion data into specific table
    :param table_name: name of the specific table
    :param data: data to be inserted
    :param id: optional. Used to update data in specific row
    :return: True if data was inserted successfully False otherwise
    """
    if not VALIDATE[table_name](data):
        error(f'Values {data} has not been inserted into table {str(table_name).capitalize()}. '
              f'Reason - didn\'t pass validation')
        return False

    if check_unique_data_presence(table_name, data):
        error(f'Values {data} has not been inserted into table {str(table_name).capitalize()}. '
              f'Reason - data already exists in unique constraint column(s)')
        print('unique')
        return False

    if not id:
        table_row = MODELS[table_name](*data.values())
        db.session.add(table_row)
        db.session.commit()
    else:
        MODELS[table_name].query.get(id).update(*dict(data).values())
        db.session.commit()
    return True


def delete_from_table(table_name, row_id):
    """
    Function performs delete operation to specific table
    :param table_name: name of specific table
    :param row_id: id of the row in table to be deleted
    :return: None
    """
    table = MODELS[table_name]
    db.session.query(table).filter(table.id == row_id).delete(synchronize_session=False)
    db.session.commit()
    info(f'Row with {row_id} id has been successfully deleted from table {str(table_name).capitalize()}')


def get_row_relation_data_from_table(table_name, row_id):
    """
    Function performs select operation on specific table. Data may also has relation information
    :param table_name: name of the specific table
    :param row_id: specific row id in table
    """
    table = MODELS[table_name]
    data = db.session.query(table).filter(table.id == row_id).first()
    if table_name in ('Orders', 'Platforms'):
        data = data.with_relations_fields()
    else:
        data = data.to_dict()

    return data
