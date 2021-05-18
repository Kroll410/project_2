def _validate_popup_value(value):
    try:
        int(value)
    except (TypeError, ValueError):
        return False
    return True


def validate_orders(data):
    try:
        play_time = float(data['play_time'])
    except (TypeError, ValueError):

        return False
    if all([play_time > 0,
            _validate_popup_value(data['Customers.id']),
            _validate_popup_value(data['Platforms.id'])]):
        return True
    else:
        return False


def validate_customers(data):
    if len(data['login_name']) > 3 and all(x.isalpha() or x.isdigit() or x == ' ' for x in data['login_name']):
        return True
    else:
        return False


def validate_platforms(data):
    try:
        return int(data['price']) > 0 and _validate_popup_value(data['Platformtypes.id'])
    except (TypeError, ValueError):
        return False


def validate_platformtypes(data):
    return False if len(data['type']) < 0 and data['type'] != ' ' else True


VALIDATE = {
    'Orders': validate_orders,
    'Platforms': validate_platforms,
    'Platformtypes': validate_platformtypes,
    'Customers': validate_customers,

}
