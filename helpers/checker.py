from logging import info
from datetime import datetime
from service.crud_operations import MODELS


def get_orders_timeout():
    """
    Function provides checking of expired orders at service.
    It retrieves all orders in current database in table `Orders` and
        looks for expired ones by `play_time` and `added_time` columns` values

    :return: list of dictionaries with data to process expired orders
    """
    orders = MODELS['Orders'].query.all()
    HOUR_SECONDS = 3600
    timeout_orders = []
    for order in orders:
        added_time = datetime.strptime(order.added_time, '%Y-%m-%d %H:%M:%S')
        curr_time = datetime.now()
        if order.play_time * HOUR_SECONDS < (curr_time - added_time).total_seconds():
            txt = ', '.join(str(x) for x in (order.id,
                                             order.play_time * 3600,
                                             curr_time, added_time,
                                             curr_time - added_time)
                            )
            info(f" Ended order: {txt}")
            timeout_orders.append({
                'order_id': order.id,
                'platform_id': order.platform_id,
                'price': order.price,
            })

    return timeout_orders
