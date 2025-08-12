import unittest
from monitor import vitals_ok

def mock_printer(msg): pass
def mock_blink(): pass

def create_single_vital(name, value, min_val, max_val):
    return [{"name": name, "value": value, "min": min_val, "max": max_val}]

class VitalBoundaryTest(unittest.TestCase):

    def test_blood_pressure_ranges(self):
        name, min_val, max_val = "blood_pressure", 80, 120
        self.assertTrue(vitals_ok(create_single_vital(name, 80, min_val, max_val), mock_printer, mock_blink))  # Lower bound
        self.assertTrue(vitals_ok(create_single_vital(name, 120, min_val, max_val), mock_printer, mock_blink)) # Upper bound
        self.assertFalse(vitals_ok(create_single_vital(name, 79.9, min_val, max_val), mock_printer, mock_blink))# Below
        self.assertFalse(vitals_ok(create_single_vital(name, 120.1, min_val, max_val), mock_printer, mock_blink))# Above

    def test_respiration_rate_ranges(self):
        name, min_val, max_val = "resp_rate", 12, 20
        self.assertTrue(vitals_ok(create_single_vital(name, 12, min_val, max_val), mock_printer, mock_blink))
        self.assertTrue(vitals_ok(create_single_vital(name, 20, min_val, max_val), mock_printer, mock_blink))
        self.assertFalse(vitals_ok(create_single_vital(name, 11.5, min_val, max_val), mock_printer, mock_blink))
        self.assertFalse(vitals_ok(create_single_vital(name, 21, min_val, max_val), mock_printer, mock_blink))

    def test_glucose_level_ranges(self):
        name, min_val, max_val = "glucose_level", 70, 140
        self.assertTrue(vitals_ok(create_single_vital(name, 70, min_val, max_val), mock_printer, mock_blink))
        self.assertTrue(vitals_ok(create_single_vital(name, 140, min_val, max_val), mock_printer, mock_blink))
        self.assertFalse(vitals_ok(create_single_vital(name, 69.9, min_val, max_val), mock_printer, mock_blink))
        self.assertFalse(vitals_ok(create_single_vital(name, 141, min_val, max_val), mock_printer, mock_blink))
															TCQ previous assessment
    def test_combined_vitals(self):
        vitals = [
            {"name": "blood_pressure", "value": 110, "min": 80, "max": 120},
            {"name": "resp_rate", "value": 16, "min": 12, "max": 20},
            {"name": "glucose_level", "value": 90, "min": 70, "max": 140}
        ]
        self.assertTrue(vitals_ok(vitals, printer=mock_printer, blinker=mock_blink))

        vitals[2]["value"] = 150  # glucose too high
        self.assertFalse(vitals_ok(vitals, printer=mock_printer, blinker=mock_blink))

if __name__ == '__main__':
    unittest.main()
	
