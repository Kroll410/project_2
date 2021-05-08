from flask import render_template, request, make_response
from werkzeug.utils import redirect

from init import app
from service import crud_operations as crud


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/show_tables')
@app.route('/show_tables/<string:table_name>', methods=["GET", "POST"])
def show_tables(table_name=None):
    if request.method == "GET":
        if table_name:
            table_name = str(table_name).capitalize()
            table_data = crud.select_from_table(table_name, show_all=True)
            is_empty = True if not table_data else False
            fields = ['id'] + list(table_data[0].keys()) if not is_empty else []

            return render_template('show-tables.html', data={
                'name': table_name,
                'table_data': enumerate(table_data),
                'fields': fields,
                'is_empty': is_empty,
            })

        else:
            table_info = {str(k): v for k, v in crud.get_all_tables_info().items()}.items()
            return render_template('show-all-tables.html', data={
                'info': enumerate(table_info)
            })


@app.route('/add/<string:table_name>', methods=["GET"])
def add(table_name):
    if request.method == 'GET':
        table_data = crud.select_from_table(table_name)
        fields = list(table_data[0].keys())
        relations = crud.get_table_relations_data(table_name)

        return render_template('add-new-row.html', data={
            'name': table_name,
            'fields': fields,
            'relations': relations,
        })
