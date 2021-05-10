from init import db
from models import Orders, Platforms


def _set_price_for_orders():
    id_prices = {}
    for val in db.session.query(Platforms.id, Platforms.price):
        val_id = val[0]
        val_price = val[1]
        id_prices.update({
            db.session.query(Orders.id, Orders.play_time).filter_by(platform_id=val_id).first(): val_price
        })

    print(id_prices)

    for key, price in id_prices.items():
        order_id, play_time = key
        Orders.query.get(order_id).price = play_time * price
        db.session.commit()



if __name__ == '__main__':
    _set_price_for_orders()
