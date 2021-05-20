
"""
Module aggregate.py consists of aggregation functions
    to be used for updating values in tables
"""

from init import db
from models.models import Orders, Platforms
from logging import info


def set_price_for_orders():
    """
    Function updates `price` column values in `Orders` table, aggregated by
        `play_time` value and price for each `platform.id`
        price = play_time * platform.price
    :return:
    """
    id_prices = {}
    for val in db.session.query(Platforms.id, Platforms.price):
        val_id = val[0]
        val_price = val[1]
        id_prices.update({
            db.session.query(Orders.id, Orders.play_time).filter_by(platform_id=val_id).first(): val_price
        })

    for key, price in id_prices.items():
        if key is None:
            continue
        order_id, play_time = key
        Orders.query.get(order_id).price = play_time * price
        info(f'Prices for `{order_id}` order was set to {play_time * price}')
        db.session.commit()


