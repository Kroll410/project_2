"""

Module validation.py consists of several function,
which validates the user inputs to be inserted into tables

"""


def _validate_popup_value(value):
    """
    Validation of value that can be chosen in popup form in `Add row` template for any table
    :param value: {value [int]: ...}
    :return: True if validation has passed, False otherwise
    """
    try:
        int(value)
    except (TypeError, ValueError):
        return False
    return True


def validate_orders(data):
    """
    Validation of values that can be entered in `Add row` template in `Orders` table
    :param data: {play_time [float]: ..., Customers.id [int]: ..., Platforms.id [int]: ...}
    :return: True if validation has passed, False otherwise
    """
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
    """
    Validation of values that can be entered in `Add row` template in `Customers` table
    :param data: {login_name [str]: ...}
    :return: True if validation has passed, False otherwise
    """
    if len(data['login_name']) > 3 and all(x.isalpha() or x.isdigit() or x == ' ' for x in data['login_name']):
        return True
    else:
        return False


def validate_platforms(data):
    """
    Validation of values that can be entered in `Add row` template in `Platforms` table
    :param data: {price[float]: ..., Platformtypes.id [int]: ...,}
    :return: True if validation has passed, False otherwise
    """
    try:
        return int(data['price']) > 0 and _validate_popup_value(data['Platformtypes.id'])
    except (TypeError, ValueError):
        return False


def validate_platformtypes(data):
    """
    Validation of values that can be entered in `Add row` template in `Platformtypes` table
    :param data: {type [str]: ...}
    :return: True if validation has passed, False otherwise
    """
    return False if len(data['type']) < 0 and data['type'] != ' ' else True


VALIDATE = {
    'Orders': validate_orders,
    'Platforms': validate_platforms,
    'Platformtypes': validate_platformtypes,
    'Customers': validate_customers,

}
