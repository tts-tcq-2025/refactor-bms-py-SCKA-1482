from check_alerts import blink_alert
from printer import default_printer

def is_out_of_range(val, min_val, max_val):
    return val < min_val or val > max_val

def handle_alert(vital, printer, blinker):
    printer(
        f"{vital['name']} out of range! "
        f"Value: {vital['value']} (Expected: {vital['min']} to {vital['max']})"
    )
    blinker()

def alert_if_critical(vitals, printer=default_printer, blinker=blink_alert):
    all_ok = True
    for vital in vitals:
        val, min_val, max_val = vital["value"], vital["min"], vital["max"]
        if is_out_of_range(val, min_val, max_val):
            handle_alert(vital, printer, blinker)
            all_ok = False
    return all_ok

def vitals_ok(vitals, printer=default_printer, blinker=blink_alert):
    return alert_if_critical(vitals, printer, blinker)	
	
