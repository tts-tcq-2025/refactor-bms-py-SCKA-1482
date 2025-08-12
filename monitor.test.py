import unittest
from monitor import vitals_ok


def mock_printer(msg): pass
def mock_blink(): pass


def create_single_vital(name, value, min_val, max_val):
    return [{"name": name, "value": value, "min": min_val, "max": max_val}]

class VitalBoundaryTest(unittest.TestCase):

    def test_blood_pressure_ranges(self):
        """Test blood pressure boundary values"""
        name, min_val, max_val = "blood_pressure", 80, 120
        test_cases = [
            (80, True),   # Lower bound
            (120, True),  # Upper bound
            (79.9, False), # Below lower bound
            (120.1, False) # Above upper bound
        ]
        for value, expected in test_cases:
            with self.subTest(value=value):
                vital = create_single_vital(name, value, min_val, max_val)
                self.assertEqual(vitals_ok(vital, mock_printer, mock_blink), expected)

    def test_respiration_rate_ranges(self):
        """Test respiration rate boundary values"""
        name, min_val, max_val = "resp_rate", 12, 20
        test_cases = [
            (12, True),   # Lower bound
            (20, True),   # Upper bound
            (11.5, False), # Below lower bound
            (21, False)    # Above upper bound
        ]
        for value, expected in test_cases:
            with self.subTest(value=value):
                vital = create_single_vital(name, value, min_val, max_val)
                self.assertEqual(vitals_ok(vital, mock_printer, mock_blink), expected)

    def test_glucose_level_ranges(self):
        """Test glucose level boundary values"""
        name, min_val, max_val = "glucose_level", 70, 140
        test_cases = [
            (70, True),    # Lower bound
            (140, True),   # Upper bound
            (69.9, False), # Below lower bound
            (141, False)   # Above upper bound
        ]
        for value, expected in test_cases:
            with self.subTest(value=value):
                vital = create_single_vital(name, value, min_val, max_val)
                self.assertEqual(vitals_ok(vital, mock_printer, mock_blink), expected)

    def test_combined_vitals(self):
        """Test multiple vitals together"""
        vitals = [
            {"name": "blood_pressure", "value": 110, "min": 80, "max": 120},
            {"name": "resp_rate", "value": 16, "min": 12, "max": 20},
            {"name": "glucose_level", "value": 90, "min": 70, "max": 140}
        ]
        self.assertTrue(vitals_ok(vitals, printer=mock_printer, blinker=mock_blink))

        vitals[2]["value"] = 150  # glucose too high
        self.assertFalse(vitals_ok(vitals, printer=mock_printer, blinker=mock_blink))

    def test_missing_fields(self):
        """Test for missing fields in vital data"""
        incomplete_vital = {"name": "heart_rate", "value": 75}
        with self.assertRaises(KeyError):
            vitals_ok([incomplete_vital], mock_printer, mock_blink)

if __name__ == '__main__':
    unittest.main()

