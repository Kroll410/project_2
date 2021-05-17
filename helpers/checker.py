from service.crud_operations import MODELS
from datetime import datetime


def get_orders_timeout():
    orders = MODELS['Orders'].query.all()
    timeout_orders = []
    for order in orders:
        added_time = datetime.strptime(order.added_time, '%Y-%m-%d %H:%M:%S')
        curr_time = datetime.now()
        # print(' | '.join(str(x) for x in (order.id, order.play_time * 3600, curr_time, added_time, delta)))
        if order.play_time * 3600 < (curr_time - added_time).total_seconds():
            timeout_orders.append({
                'order_id': order.id,
                'platform_id': order.platform_id,
                'price': order.price,
            })

    return timeout_orders
