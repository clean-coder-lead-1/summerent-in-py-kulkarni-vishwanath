
def infer_breach(value, temperature_range):
    """Checks the breach based on the temperature value and the range.

    :param value: temperature threshold
    :type value: int
    :param temperature_range: temperature range
    :type temperature_range: list
    :return: breach
    :rtype: string
    """
    if value < temperature_range[0]:
        return 'TOO_LOW'
    if value > temperature_range[1]:
        return 'TOO_HIGH'
    return 'NORMAL'


def classify_temperature_breach(cooling_type, temperature_inc):
    """Classify the temperature breach based on cooling type and temperature threshold.

    :param cooling_type: Type of cooling
    :type cooling_type: string
    :param temperature_inc: Temperature threshold
    :type temperature_inc: int
    :return: Breach
    :rtype: string
    """
    temperature_range = get_temperature_range(cooling_type)
    return infer_breach(temperature_inc, temperature_range)

def get_temperature_range(cooling_type):
    """Get the temperature range based on the cooling type.

    :param cooling_type: Type of cooling
    :type cooling_type: string
    :return: Temperature range
    :rtype: list
    """
    if cooling_type == 'PASSIVE_COOLING':
        return [0, 35]
    elif cooling_type == 'MED_ACTIVE_COOLING':
        return [0, 40]
    elif cooling_type == 'HI_ACTIVE_COOLING':
        return [0, 45]
    else:
        raise ValueError("Invalid cooling type")

def check_and_alert(alert_target, battery_char, temperature_inc):
    """Send mail to controller or email id based on alert mechanism.

    :param alert_target: whom to alert.
    :type alert_target: string
    :param battery_char: cooling type
    :type battery_char: int
    :param temperature_inc: temperature threshold
    :type temperature_inc: int
    """
    breach_type = classify_temperature_breach(battery_char['coolingType'], temperature_inc)
    if alert_target == 'TO_CONTROLLER':
        send_to_controller(breach_type)
    elif alert_target == 'TO_EMAIL':
        send_to_email(breach_type)


def send_to_controller(breach_type):
    """Send information to controller based on the breach type.

    :param breach_type: breach type
    :type breach_type: string
    :return: content to controller.
    :rtype: string
    """
    header = 0xfeed
    print(f'{header}, {breach_type}')
    return f'{header}, {breach_type}'


def send_to_email(breach_type):
    """Send mail to recepient based on breach type.

    :param breach_type: breach type
    :type breach_type: string
    :return: mail content to recepient
    :rtype: string
    """
    recepient = "a.b@c.com"
    if breach_type == 'TOO_LOW':
        message = f'Hi {recepient}, the temperature is {breach_type}'
    elif breach_type == 'TOO_HIGH':
        message = f'Hi {recepient}, the temperature is {breach_type}'
    print (message)
    return message
