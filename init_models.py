from models import Customers, Orders, Platforms, Platformtypes, MODELS
from service import crud_operations as crud
from init import db
from config import Config

con = db.create_engine(Config.SQLALCHEMY_DATABASE_URI, {})
meta = db.MetaData(bind=con)
from service import aggregate


def init_db():
    db.drop_all()
    db.create_all()
    customer = Customers('some_guy')
    db.session.add(customer)
    customer = Customers('another_guy')
    db.session.add(customer)
    db.session.commit()

    platform_type = Platformtypes('PC')
    db.session.add(platform_type)
    db.session.commit()

    platform = Platforms(type_id=1, price=199)
    db.session.add(platform)
    db.session.commit()

    order = Orders(2.0, customer.id, platform.id)
    db.session.add(order)
    db.session.commit()

    # order = Orders(2.0, 1, 2)
    # db.session.add(order)
    # db.session.commit()
    aggregate._set_price_for_orders()
