import unittest
from monitor import vitals_ok_with_warning

def mock_alert_handler(msg):
    print(f"[MOCK ALERT] {msg}")

class TestVitalsMonitorWithWarnings(unittest.TestCase):

    def test_all_vitals_normal(self):
        # All vitals well inside limits, no alerts or warnings
        self.assertTrue(vitals_ok_with_warning(98.6, 72, 98, mock_alert_handler))

    def test_temperature_low_alert(self):
        # Below min, should trigger alert
        self.assertFalse(vitals_ok_with_warning(94, 72, 98, mock_alert_handler))

    def test_temperature_low_warning(self):
        # Within warning tolerance near low limit
        # 95 is min, tolerance = 1.5% of 102 = 1.53, so warning if temp in 95 - 96.53
        self.assertFalse(vitals_ok_with_warning(95.5, 72, 98, mock_alert_handler))

    def test_temperature_high_alert(self):
        # Above max, should trigger alert
        self.assertFalse(vitals_ok_with_warning(103, 72, 98, mock_alert_handler))

    def test_temperature_high_warning(self):
        # Within warning tolerance near high limit
        self.assertFalse(vitals_ok_with_warning(101.0, 72, 98, mock_alert_handler))

    def test_pulse_low_alert(self):
        self.assertFalse(vitals_ok_with_warning(98.6, 55, 98, mock_alert_handler))

    def test_pulse_low_warning(self):
        # Min 60, tolerance 1.5% of 100 = 1.5, warning if pulse in 60 to 61.5
        self.assertFalse(vitals_ok_with_warning(60.5, 60.5, 98, mock_alert_handler))

    def test_pulse_high_alert(self):
        self.assertFalse(vitals_ok_with_warning(98.6, 101, 98, mock_alert_handler))

    def test_pulse_high_warning(self):
        # Warning near high limit 100 down to 98.5
        self.assertFalse(vitals_ok_with_warning(98.6, 99, 98, mock_alert_handler))

    def test_spo2_low_alert(self):
        self.assertFalse(vitals_ok_with_warning(98.6, 72, 89, mock_alert_handler))

    def test_spo2_low_warning(self):
        # Min 90, tolerance 1.5% of 100 = 1.5, warning between 90 and 91.5
        self.assertFalse(vitals_ok_with_warning(98.6, 72, 90.5, mock_alert_handler))

    def test_multiple_abnormal(self):
        self.assertFalse(vitals_ok_with_warning(104, 105, 85, mock_alert_handler))

if __name__ == '__main__':
    unittest.main()
