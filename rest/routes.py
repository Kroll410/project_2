from flask import request
from flask_restful import Resource
from werkzeug.utils import redirect

from models import Orders, Customers, Platforms, Platformtypes
from init import db, api
from service import crud_operations as crud


class OrderListApi(Resource):
    def get(self, id=None):
        orders = crud.select_from_table('orders', id)

        if not orders:
            return {}, 404

        return orders, 200

    def post(self):
        if request.form:
            crud.insert_into_table('Orders', request.form)
            return redirect('show_tables/Orders')

    def patch(self):
        pass

    def put(self):
        pass

    def delete(self, id):
        if id:
            crud.delete_from_table('Orders', id)


class CustomerListApi(Resource):
    def get(self, id=None):
        if not id:
            customers = db.session.query(Customers)
            return [el.to_dict() for el in customers], 200

        customer = db.session.query(Customers).filter_by(id=id).first()
        if not customer:
            return {}, 404

        return customer.to_dict(), 200

    def post(self):
        if request.form:
            crud.insert_into_table('Customers', request.form)
            return redirect('show_tables/Customers')

    def patch(self):
        pass

    def put(self):
        pass

    def delete(self, id):
        print(id)


class PlatformListApi(Resource):
    def get(self, id=None):
        if not id:
            platforms = db.session.query(Platforms)
            return [el.to_dict() for el in platforms], 200

        platform = db.session.query(Platforms).filter_by(id=id).first()
        if not platform:
            return {}, 404

        return platform.to_dict(), 200

    def post(self):
        if request.form:
            crud.insert_into_table('Platforms', request.form)
            return redirect('show_tables/Platforms')

    def patch(self):
        pass

    def put(self):
        pass

    def delete(self):
        pass


class PlatformTypeListApi(Resource):
    def get(self, id=None):
        if not id:
            platforms_types = db.session.query(Platformtypes)
            return [el.to_dict() for el in platforms_types], 200

        platform_type = db.session.query(Platformtypes).filter_by(id=id).first()
        if not platform_type:
            return {}, 404

        return platform_type.to_dict(), 200

    def post(self):
        if request.form:
            crud.insert_into_table('Platformtypes', request.form)
            return redirect('show_tables/Platformtypes')

    def patch(self):
        pass

    def put(self):
        pass

    def delete(self):
        pass


api.add_resource(OrderListApi, '/orders', '/orders/<id>', strict_slashes=False)
api.add_resource(CustomerListApi, '/customers', '/customers/<id>', strict_slashes=False)
api.add_resource(PlatformListApi, '/platforms', '/platforms/<id>', strict_slashes=False)
api.add_resource(PlatformTypeListApi, '/platformtypes', '/platformtypes/<id>', strict_slashes=False)
