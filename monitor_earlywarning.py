def default_display_warning(msg):
    print(f"WARNING: {msg}")

def get_warning_ranges(min_val, max_val, tolerance_percent=1.5):
    tolerance = (max_val - min_val) * tolerance_percent / 100
    return (min_val, min_val + tolerance), (max_val - tolerance, max_val)

def check_vitals(vitals, status_func, alert_handler):
    """
    vitals: list of dicts with keys 'name', 'value', 'min', 'max'
    status_func: function that returns 'NORMAL', 'WARNING_LOW', 'WARNING_HIGH', 'ALERT_LOW', 'ALERT_HIGH'
    alert_handler: function to handle alert or warning messages
    Returns True if all vitals are normal, False otherwise.
    """
    all_ok = True
    for vital in vitals:
        status = status_func(vital)
        if status == 'NORMAL':
            continue
        all_ok = False
        message = f"{vital['name']} {status} Value: {vital['value']}"
        alert_handler(message)
    return all_ok

def simple_status(vital):
    if vital['value'] < vital['min']:
        return 'ALERT_LOW'
    elif vital['value'] > vital['max']:
        return 'ALERT_HIGH'
    return 'NORMAL'

def warning_status(vital):
    low_warn_range, high_warn_range = get_warning_ranges(vital['min'], vital['max'])
    val = vital['value']
    if val < vital['min']:
        return 'ALERT_LOW'
    elif val > vital['max']:
        return 'ALERT_HIGH'
    elif low_warn_range[0] <= val <= low_warn_range[1]:
        return 'WARNING_LOW'
    elif high_warn_range[0] <= val <= high_warn_range[1]:
        return 'WARNING_HIGH'
    return 'NORMAL'

def vitals_ok(temperature, pulseRate, spo2, alert_handler=default_display_warning):
    vitals = [
        {'name': 'Temperature', 'value': temperature, 'min': 95, 'max': 102},
        {'name': 'Pulse Rate', 'value': pulseRate, 'min': 60, 'max': 100},
        {'name': 'SpO2', 'value': spo2, 'min': 90, 'max': 100},
    ]
    return check_vitals(vitals, simple_status, alert_handler)

def vitals_ok_with_warning(temperature, pulseRate, spo2, alert_handler=default_display_warning):
    vitals = [
        {'name': 'Temperature', 'value': temperature, 'min': 95, 'max': 102},
        {'name': 'Pulse Rate', 'value': pulseRate, 'min': 60, 'max': 100},
        {'name': 'SpO2', 'value': spo2, 'min': 90, 'max': 100},
    ]
    return check_vitals(vitals, warning_status, alert_handler)
