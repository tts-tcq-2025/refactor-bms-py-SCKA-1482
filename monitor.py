
from time import sleep
import sys


def validate_vitals(temperature, pulseRate, spo2):
    if temperature > 102 or temperature < 95:
        return False, 'Temperature critical!'
    if pulseRate < 60 or pulseRate > 100:
        return False, 'Pulse Rate is out of range!'
    if spo2 < 90:
        return False, 'Oxygen Saturation out of range!'
    return True, 'All vitals normal.'

def alert_blink(message, blink_count=6):
    print(message)
    for _ in range(blink_count):
        print('\r* ', end='')
        sys.stdout.flush()
        sleep(1)
        print('\r *', end='')
        sys.stdout.flush()
        sleep(1)
    print()  # Move to next line after blinking

def vitals_ok(temperature, pulseRate, spo2):
    ok, message = validate_vitals(temperature, pulseRate, spo2)
    if not ok:
        alert_blink(message)
    return ok   
  
