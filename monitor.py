
from time import sleep
import sys


def validate_temperature(temp):
  if temp>102 or temp<95:
    return False,'Temperature Critical!'
  return True,''

def validate_pulse(pulse):
  if pulse<60 or pulse>100:
    return False,'Pulse out of range!'
  return True,''

def validate_spo2(spo2):
  if spo2<90:
    return False,'Oxygen Saturation out of range!'
  return True,''  
   

def vitals_vitals(temperature,pulseRate,spo2):
  for validate in (validate_temperature,validate_pulse,validate_spo2):
    ok,message = validate(temperature if validate == validate_temperature else pulseRate if validate == validate_pulse else spo2)
    if not ok:
      return False,message
  return True,'All vitals normal.'    
  
