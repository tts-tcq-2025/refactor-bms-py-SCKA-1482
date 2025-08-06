import unittest
from monitor import vitals_ok, validate_vitals

def no_alert(_):
    pass  

class MonitorTest(unittest.TestCase):
    def test_vitals_ok_no_alert(self):
        self.assertFalse(vitals_ok(94, 70, 98, alert_func=no_alert))
        self.assertTrue(vitals_ok(98.6, 75, 98, alert_func=no_alert))

    def test_validate_vitals(self):
        self.assertEqual(validate_vitals(94, 70, 98), (False, 'Temperature critical!'))
        self.assertEqual(validate_vitals(98.6, 75, 98), (True, 'All vitals normal.'))

if __name__ == '__main__':
    unittest.main()



