import sys
from time import sleep

# --- I/O Handler (can be mocked for testing) ---
def default_display_warning(message):
    print(message)
    for _ in range(6):
        print('\r* ', end='')
        sys.stdout.flush()
        sleep(1)
        print('\r *', end='')
        sys.stdout.flush()
        sleep(1)

# --- Core logic ---

def is_out_of_range(value, min_val, max_val):
    return value < min_val or value > max_val

def get_abnormal_vitals(vitals):
    """Check all vitals and return the ones out of range."""
    abnormal = []
    for vital in vitals:
        if is_out_of_range(vital['value'], vital['min'], vital['max']):
            abnormal.append(vital)
    return abnormal

def alert_abnormal_vitals(vitals, alert_handler=default_display_warning):
    abnormal_vitals = get_abnormal_vitals(vitals)
    for vital in abnormal_vitals:
        alert_handler(f"{vital['name']} out of range! Value: {vital['value']} (Expected: {vital['min']} - {vital['max']})")
    return len(abnormal_vitals) == 0

# --- Interface Function ---
def vitals_ok(temperature, pulseRate, spo2, alert_handler=default_display_warning):
    vitals = [
        {"name": "temperature", "value": temperature, "min": 95, "max": 102},
        {"name": "pulse rate", "value": pulseRate, "min": 60, "max": 100},
        {"name": "SpO2", "value": spo2, "min": 90, "max": 100}
    ]
    return alert_abnormal_vitals(vitals, alert_handler)
