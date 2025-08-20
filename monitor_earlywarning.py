def default_display_warning(message):
    print(f"WARNING: {message}")

def get_warning_ranges():
    return {
        'temperature': (36.1, 37.2),
        'pulseRate': (60, 100),
        'spo2': (95, 100)
    }

def check_vitals(temperature, pulseRate, spo2):
    warning_ranges = get_warning_ranges()
    vitals = {
        'temperature': 'normal',
        'pulseRate': 'normal',
        'spo2': 'normal'
    }

    # Temperature
    low, high = warning_ranges['temperature']
    if temperature < low - 1.0:
        vitals['temperature'] = 'alert'
    elif temperature < low:
        vitals['temperature'] = 'warning'
    elif temperature > high + 1.0:
        vitals['temperature'] = 'alert'
    elif temperature > high:
        vitals['temperature'] = 'warning'

    # Pulse Rate
    low, high = warning_ranges['pulseRate']
    if pulseRate < low - 10:
        vitals['pulseRate'] = 'alert'
    elif pulseRate < low:
        vitals['pulseRate'] = 'warning'
    elif pulseRate > high + 10:
        vitals['pulseRate'] = 'alert'
    elif pulseRate > high:
        vitals['pulseRate'] = 'warning'

    # SPO2
    low, high = warning_ranges['spo2']
    if spo2 < low - 5:
        vitals['spo2'] = 'alert'
    elif spo2 < low:
        vitals['spo2'] = 'warning'

    return vitals

def alert_vitals_with_warning(vitals, alert_handler=default_display_warning):
    for vital, status in vitals.items():
        if status == 'alert':
            alert_handler(f"{vital} is at alert level!")
        elif status == 'warning':
            alert_handler(f"{vital} is at warning level.")

def vitals_ok(temperature, pulseRate, spo2, alert_handler=None, consider_warnings_as_abnormal=False):
    vitals = check_vitals(temperature, pulseRate, spo2)
    if alert_handler:
        alert_vitals_with_warning(vitals, alert_handler)
    if consider_warnings_as_abnormal:
        return all(status == 'normal' for status in vitals.values())
    else:
        # warnings treated as ok
        return all(status in ('normal', 'warning') for status in vitals.values())
