import unittest

from src.car import Car
from src.validator import Validator


class MyTestCase(unittest.TestCase):
    def test_holiday(self):
        date = '23-05-2022'
        hour = "09:00"
        vehicle = Car("PDC-3261")
        actual = Validator(vehicle, date, hour).is_driving_allowed()
        expected = True
        self.assertEqual(actual, expected)

    def test_weekend(self):
        date = "16-04-2022"
        hour = "09:00"
        vehicle = Car("GDC-3261")
        actual = Validator(vehicle, date, hour).is_driving_allowed()
        expected = True
        self.assertEqual(actual, expected)

    def test_not_allowed_morning_edge(self):
        date = "14-06-2022"
        hour = "06:00"
        vehicle = Car("PBW-1364")
        actual = Validator(vehicle, date, hour).is_driving_allowed()
        expected = False
        self.assertEqual(actual, expected)

    def test_not_allowed_night_edge(self):
        date = "27-05-2022"
        hour = "21:00"
        vehicle = Car("XBW-1860")
        actual = Validator(vehicle, date, hour).is_driving_allowed()
        expected = False
        self.assertEqual(actual, expected)

if __name__ == '__main__':
    unittest.main()
