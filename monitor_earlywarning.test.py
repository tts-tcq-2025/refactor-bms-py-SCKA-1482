import unittest
from monitor_earlywarning import vitals_ok, vitals_ok_with_warning

def mock_alert_handler(msg):
    print(f"[MOCK ALERT] {msg}")

class TestVitalsMonitorSimple(unittest.TestCase):

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


class TestVitalsMonitorWithWarnings(unittest.TestCase):

    def test_all_vitals_normal(self):
        self.assertTrue(vitals_ok_with_warning(98.6, 72, 98, mock_alert_handler))

    def test_temperature_low_alert(self):
        self.assertFalse(vitals_ok_with_warning(94, 72, 98, mock_alert_handler))

    def test_temperature_low_warning(self):
        # 95 is min, tolerance 1.5% of (102-95=7) = 0.105, so warning if temp in 95 - 95.105 (approx)
        self.assertFalse(vitals_ok_with_warning(95.05, 72, 98, mock_alert_handler))

    def test_temperature_high_alert(self):
        self.assertFalse(vitals_ok_with_warning(103, 72, 98, mock_alert_handler))

    def test_temperature_high_warning(self):
        self.assertFalse(vitals_ok_with_warning(101.0, 72, 98, mock_alert_handler))

    def test_pulse_low_alert(self):
        self.assertFalse(vitals_ok_with_warning(98.6, 55, 98, mock_alert_handler))

    def test_pulse_low_warning(self):
        self.assertFalse(vitals_ok_with_warning(98.6, 60.5, 98, mock_alert_handler))

    def test_pulse_high_alert(self):
        self.assertFalse(vitals_ok_with_warning(98.6, 101, 98, mock_alert_handler))

    def test_pulse_high_warning(self):
        self.assertFalse(vitals_ok_with_warning(98.6, 99, 98, mock_alert_handler))

    def test_spo2_low_alert(self):
        self.assertFalse(vitals_ok_with_warning(98.6, 72, 89, mock_alert_handler))

    def test_spo2_low_warning(self):
        self.assertFalse(vitals_ok_with_warning(98.6, 72, 90.5, mock_alert_handler))

    def test_multiple_abnormal(self):
        self.assertFalse(vitals_ok_with_warning(104, 105, 85, mock_alert_handler))


if __name__ == '__main__':
    unittest.main()
