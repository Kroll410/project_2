from flask import request, url_for
from flask_restful import Resource
from werkzeug.utils import redirect
from init import api
from service import crud_operations as crud, aggregate


class OrderListApi(Resource):
    def get(self, id=None):
        orders = crud.select_from_table('orders', id)

        if not orders:
            return {}, 404

        return orders, 200

    def post(self, id=None):
        if request.form:
            if id:
                crud.insert_into_table('Orders', request.form, id=id)
            else:
                crud.insert_into_table('Orders', request.form)

            aggregate._set_price_for_orders()
            return redirect('../show_tables/Orders')

    def delete(self, id):
        if id:
            crud.delete_from_table('Orders', id)
            return redirect(url_for('show_tables'))


class CustomerListApi(Resource):
    def get(self, id=None):
        customers = crud.select_from_table('customers', id)

        if not customers:
            return {}, 404

        return customers, 200

    def post(self, id=None):
        if id:
            crud.insert_into_table('Customers', request.form, id=id)
        else:
            crud.insert_into_table('Customers', request.form)

        return redirect('../show_tables/Customers')

    def delete(self, id):
        if id:
            crud.delete_from_table('Customers', id)
            return redirect('customers')


class PlatformListApi(Resource):
    def get(self, id=None):
        platforms = crud.select_from_table('platforms', id)

        if not platforms:
            return {}, 404

        return platforms, 200

    def post(self, id=None):
        if id:
            crud.insert_into_table('Platforms', request.form, id=id)
        else:
            crud.insert_into_table('Customers', request.form)

        return redirect('../show_tables/Platforms')

    def delete(self, id):
        if id:
            crud.delete_from_table('Platforms', id)
            return redirect('platforms')


class PlatformTypeListApi(Resource):
    def get(self, id=None):
        platformtypes = crud.select_from_table('platformtypes', id)

        if not platformtypes:
            return {}, 404

        return platformtypes, 200

    def post(self, id=None):
        if id:
            crud.insert_into_table('Platformtypes', request.form, id=id)
        else:
            crud.insert_into_table('Platformtypes', request.form)

        return redirect('../show_tables/PlatformTypes')

    def delete(self, id):
        if id:
            crud.delete_from_table('Platformtypes', id)
            return redirect('platformtypes')


api.add_resource(OrderListApi, '/orders', '/orders/<id>', strict_slashes=False)
api.add_resource(CustomerListApi, '/customers', '/customers/<id>', strict_slashes=False)
api.add_resource(PlatformListApi, '/platforms', '/platforms/<id>', strict_slashes=False)
api.add_resource(PlatformTypeListApi, '/platformtypes', '/platformtypes/<id>', strict_slashes=False)
