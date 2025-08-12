import unittest
from vitals_monitor import vitals_ok

def mock_alert_handler(msg):
    # Simulate alert handling without sleep or print
    print(f"[MOCK ALERT] {msg}")

class TestVitalsMonitor(unittest.TestCase):

    def test_all_vitals_normal(self):
        self.assertTrue(vitals_ok(98.6, 72, 98, mock_alert_handler))

    def test_temperature_low(self):
        self.assertFalse(vitals_ok(94, 72, 98, mock_alert_handler))

    def test_temperature_high(self):
        self.assertFalse(vitals_ok(103, 72, 98, mock_alert_handler))

    def test_pulse_low(self):
        self.assertFalse(vitals_ok(98.6, 55, 98, mock_alert_handler))

    def test_pulse_high(self):
        self.assertFalse(vitals_ok(98.6, 101, 98, mock_alert_handler))

    def test_spo2_low(self):
        self.assertFalse(vitals_ok(98.6, 72, 89, mock_alert_handler))

    def test_multiple_abnormal(self):
        self.assertFalse(vitals_ok(104, 105, 85, mock_alert_handler))

if __name__ == '__main__':
    unittest.main()
