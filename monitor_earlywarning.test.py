import pytest
from monitor_earlywarning import vitals_ok, check_vitals

alerts = []
def mock_alert_handler(message):
    alerts.append(message)

def test_all_vitals_normal():
    alerts.clear()
    assert vitals_ok(36.5, 70, 97, alert_handler=mock_alert_handler)
    assert alerts == []

def test_temperature_low_alert():
    alerts.clear()
    temp = 34.5  # alert low
    assert not vitals_ok(temp, 70, 97, alert_handler=mock_alert_handler)
    assert any("temperature is at alert level" in msg for msg in alerts)

def test_temperature_low_warning():
    alerts.clear()
    temp = 35.9  # warning low
    assert vitals_ok(temp, 70, 97, alert_handler=mock_alert_handler)
    assert any("temperature is at warning level" in msg for msg in alerts)

def test_temperature_high_alert():
    alerts.clear()
    temp = 39.0  # alert high
    assert not vitals_ok(temp, 70, 97, alert_handler=mock_alert_handler)
    assert any("temperature is at alert level" in msg for msg in alerts)

def test_temperature_high_warning():
    alerts.clear()
    temp = 37.5  # warning high
    assert vitals_ok(temp, 70, 97, alert_handler=mock_alert_handler)
    assert any("temperature is at warning level" in msg for msg in alerts)

def test_pulse_low_alert():
    alerts.clear()
    pulse = 40  # alert low
    assert not vitals_ok(36.5, pulse, 97, alert_handler=mock_alert_handler)
    assert any("pulseRate is at alert level" in msg for msg in alerts)

def test_pulse_low_warning():
    alerts.clear()
    pulse = 55  # warning low
    assert vitals_ok(36.5, pulse, 97, alert_handler=mock_alert_handler)
    assert any("pulseRate is at warning level" in msg for msg in alerts)

def test_pulse_high_alert():
    alerts.clear()
    pulse = 115  # alert high
    assert not vitals_ok(36.5, pulse, 97, alert_handler=mock_alert_handler)
    assert any("pulseRate is at alert level" in msg for msg in alerts)

def test_pulse_high_warning():
    alerts.clear()
    pulse = 105  # warning high
    assert vitals_ok(36.5, pulse, 97, alert_handler=mock_alert_handler)
    assert any("pulseRate is at warning level" in msg for msg in alerts)

def test_spo2_low_alert():
    alerts.clear()
    spo2 = 89  # alert low
    assert not vitals_ok(36.5, 70, spo2, alert_handler=mock_alert_handler)
    assert any("spo2 is at alert level" in msg for msg in alerts)

def test_spo2_low_warning():
    alerts.clear()
    spo2 = 93  # warning low
    assert vitals_ok(36.5, 70, spo2, alert_handler=mock_alert_handler)
    assert any("spo2 is at warning level" in msg for msg in alerts)

def test_multiple_abnormal():
    alerts.clear()
    temp = 34.0  # alert low temp
    pulse = 110  # warning high pulse
    spo2 = 93    # warning low spo2
    result = vitals_ok(temp, pulse, spo2, alert_handler=mock_alert_handler)
    # alert expected, so vitals_ok should be False because alert present
    assert not result
    assert any("temperature is at alert level" in msg for msg in alerts)
    assert any("pulseRate is at warning level" in msg for msg in alerts)
    assert any("spo2 is at warning level" in msg for msg in alerts)
