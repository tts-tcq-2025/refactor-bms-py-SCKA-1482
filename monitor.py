from check_alerts import blink_alert
from printer import default_printer


def is_out_of_range(val, min_val, max_val):
    return val < min_val or val > max_val


def get_abnormal_vitals(vitals):
    """Returns vitals that are out of range."""
    return [vital for vital in vitals if is_out_of_range(vital['value'], vital['min'], vital['max'])]


def handle_alert(vital, printer, blinker):
    """Prints an alert message and triggers a blinking action."""
    printer(
        f"{vital['name']} out of range! "
        f"Value: {vital['value']} (Expected: {vital['min']} to {vital['max']})"
    )
    blinker()


def alert_on_abnormal(vitals, printer=default_printer, blinker=blink_alert):
    """Checks and alerts if any vitals are abnormal."""
    abnormal_vitals = get_abnormal_vitals(vitals)
    for vital in abnormal_vitals:
        handle_alert(vital, printer, blinker)
    return len(abnormal_vitals) == 0  # True if all vitals OK


vitals_ok = alert_on_abnormal

def vitals_ok(vitals, printer=default_printer, blinker=blink_alert):
    return alert_if_critical(vitals, printer, blinker)	
	
