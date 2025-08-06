
from time import sleep
import sys


from time import sleep
import sys

def validate_vitals(temperature, pulseRate, spo2):
    checks = [
        (lambda t, p, s: t > 102 or t < 95, 'Temperature critical!'),
        (lambda t, p, s: p < 60 or p > 100, 'Pulse Rate is out of range!'),
        (lambda t, p, s: s < 90, 'Oxygen Saturation out of range!'),
    ]
    
    for check, message in checks:
        if check(temperature, pulseRate, spo2):
            return False, message
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
    print()  

def vitals_ok(temperature, pulseRate, spo2, alert_func=alert_blink):
    ok, message = validate_vitals(temperature, pulseRate, spo2)
    if not ok and alert_func:
        alert_func(message)
    return ok
  
  
