import pytest
from monitor_earlywarning import (
    check_vitals,
    vitals_ok,
    alert_vitals_with_warning,
)

class MockAlertHandler:
    def __init__(self):
        self.alerts = []

    def __call__(self, message):
        self.alerts.append(message)

@pytest.mark.parametrize(
    "temp, pulse, spo2, expected_warnings",
    [
        (37.0, 80, 95, []),
        (35.5, 80, 95, ["Temperature low warning"]),
        (39.0, 80, 95, ["Temperature high warning"]),
        (37.0, 50, 95, ["Pulse rate low warning"]),
        (37.0, 110, 95, ["Pulse rate high warning"]),
        (37.0, 80, 85, ["SpO2 low warning"]),
        (35.0, 50, 85, ["Temperature low warning", "Pulse rate low warning", "SpO2 low warning"]),
    ],
)
def test_check_vitals(temp, pulse, spo2, expected_warnings):
    alerts = check_vitals(temp, pulse, spo2)
    assert sorted(alerts) == sorted(expected_warnings)

@pytest.mark.parametrize(
    "temp, pulse, spo2, expected_ok",
    [
        (37.0, 80, 95, True),
        (35.5, 80, 95, False),
        (39.0, 80, 95, False),
        (37.0, 50, 95, False),
        (37.0, 110, 95, False),
        (37.0, 80, 85, False),
    ],
)
def test_vitals_ok(temp, pulse, spo2, expected_ok):
    assert vitals_ok(temp, pulse, spo2) == expected_ok

def test_alert_vitals_with_warning_calls_handler():
    handler = MockAlertHandler()
    alert_vitals_with_warning(35.5, 50, 85, handler)
    assert sorted(handler.alerts) == sorted([
        "Temperature low warning",
        "Pulse rate low warning",
        "SpO2 low warning",
    ])

def test_alert_vitals_with_warning_no_warnings():
    handler = MockAlertHandler()
    alert_vitals_with_warning(37.0, 80, 95, handler)
    assert handler.alerts == []
