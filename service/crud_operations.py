import config
from init import db
from models.models import MODELS
from helpers.validation import VALIDATE

con = db.create_engine(config.Config.SQLALCHEMY_DATABASE_URI, {})
meta = db.MetaData(bind=con)


def select_from_table(table_name, id=None, show_all=False):
    if id is None:
        table = db.session.query(MODELS[str(table_name).capitalize()]).all()
        return [el.get_info_dict() for el in table] if show_all else [el.to_dict() for el in table]

    row = db.session.query(MODELS[str(table_name).capitalize()]).filter_by(id=id).first()
    if not row:
        return {}

    return row.get_info_dict() if show_all else row.to_dict()


def get_all_tables_info() -> dict:
    inspector = db.inspect(con)
    tables = inspector.get_table_names()

    data = {}
    for table in tables:
        data.update({table: []})
        for column in inspector.get_columns(table):
            data[table].append(column['name'])

    return data


def get_table_relations_data(table_name):
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


def get_table_fields(table_name):
    table = MODELS[table_name]
    return table.to_dict(table).keys()


def get_table_info_fields(table_name):
    table = MODELS[table_name]
    return table.get_info_dict(table).keys()


def check_unique_data_presence(table_name, data, row_id=None):
    table = MODELS[table_name]
    if row_id:
        for column_name, value in select_from_table(table_name, row_id).items():
            c = table.__table__.columns.get(column_name)
            if c.unique and data[column_name] == value:
                return True
    else:
        for row in select_from_table(table_name, row_id):
            for column_name, value in row.items():
                c = table.__table__.columns.get(column_name)
                if c.unique and data[column_name] == value:
                    return True

    return False


def insert_into_table(table_name, data, id=None):
    if not VALIDATE[table_name](data):
        return False

    if check_unique_data_presence(table_name, data, id):
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
    table = MODELS[table_name]
    db.session.query(table).filter(table.id == row_id).delete(synchronize_session=False)
    db.session.commit()


def get_row_data_from_table(table_name, row_id):
    table = MODELS[table_name]
    data = db.session.query(table).filter(table.id == row_id).first()
    if table_name in ('Orders', 'Platforms'):
        data = data.with_relations_fields()
    else:
        data = data.to_dict()

    return data
