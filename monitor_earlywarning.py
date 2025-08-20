def get_warning_ranges(min_val, max_val, tolerance_percent=1.5):
    tolerance = max_val * (tolerance_percent / 100)
    near_min_upper = min_val + tolerance
    near_max_lower = max_val - tolerance
    return near_min_upper, near_max_lower

def get_vital_status(value, min_val, max_val):
    near_min_upper, near_max_lower = get_warning_ranges(min_val, max_val)
    
    if value < min_val:
        return "ALERT_LOW"
    elif value < near_min_upper:
        return "WARNING_LOW"
    elif value > max_val:
        return "ALERT_HIGH"
    elif value > near_max_lower:
        return "WARNING_HIGH"
    else:
        return "NORMAL"

def alert_vital(vital, alert_handler=default_display_warning):
    status = get_vital_status(vital['value'], vital['min'], vital['max'])
    name = vital['name']
    value = vital['value']
    min_val = vital['min']
    max_val = vital['max']
    tolerance = max_val * 0.015

    if status == "ALERT_LOW":
        alert_handler(f"{name} critically low! Value: {value} (Expected above {min_val})")
    elif status == "WARNING_LOW":
        alert_handler(f"Warning: {name} approaching low limit. Value: {value} (Near {min_val} ± {tolerance:.2f})")
    elif status == "ALERT_HIGH":
        alert_handler(f"{name} critically high! Value: {value} (Expected below {max_val})")
    elif status == "WARNING_HIGH":
        alert_handler(f"Warning: {name} approaching high limit. Value: {value} (Near {max_val} ± {tolerance:.2f})")
    # Normal needs no alert

def alert_vitals_with_warning(vitals, alert_handler=default_display_warning):
    any_alerts = False
    for vital in vitals:
        status = get_vital_status(vital['value'], vital['min'], vital['max'])
        if status.startswith("ALERT") or status.startswith("WARNING"):
            alert_vital(vital, alert_handler)
            any_alerts = True
    return not any_alerts

def vitals_ok_with_warning(temperature, pulseRate, spo2, alert_handler=default_display_warning):
    vitals = [
        {"name": "temperature", "value": temperature, "min": 95, "max": 102},
        {"name": "pulse rate", "value": pulseRate, "min": 60, "max": 100},
        {"name": "SpO2", "value": spo2, "min": 90, "max": 100}
    ]
    return alert_vitals_with_warning(vitals, alert_handler)
