import unittest
from monitor import vitals_ok

class MonitorTest(unittest.TestCase):
    def test_temperature_out_of_range(self):
        self.assertFalse(vitals_ok(94, 70, 95))
        self.assertFalse(vitals_ok(103, 70, 95))

    def test_pulse_rate_out_of_range(self):
        self.assertFalse(vitals_ok(98.6, 59, 95))
        self.assertFalse(vitals_ok(98.6, 101, 95))
    
    def test_spo2_out_of_range(self):
        self.assertFalse(vitals_ok(98.6, 70, 89))
    
    def test_all_vitals_ok(self):
        self.assertTrue(vitals_ok(98.6, 70, 95))
    
    def test_multiple_vitals_out_of_range(self):
        self.assertFalse(vitals_ok(94, 59, 85))
        self.assertFalse(vitals_ok(103, 101, 89))
    
    def test_edge_values(self):
        self.assertFalse(vitals_ok(95, 70, 95))
        self.assertFalse(vitals_ok(102, 70, 95))
        self.assertFalse(vitals_ok(98.6, 60, 95))
        self.assertFalse(vitals_ok(98.6, 100, 95))
        self.assertTrue(vitals_ok(96, 70, 90))

if __name__ == '__main__':
    unittest.main()
	
