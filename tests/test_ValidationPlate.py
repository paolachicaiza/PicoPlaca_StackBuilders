import unittest

from src.input_reader import InputReader
from src.driving_condition_validator import DrivingConditionValidator


class MyTestCase(unittest.TestCase):
    def get_driving_condition(self):
        input_data = InputReader()
        input_data.read_data("data.txt")
        input_data.parse_lines()
        plate = input_data.plate_str
        date = input_data.date_str
        hour = input_data.hour_str

        plate = DrivingConditionValidator(plate, date, hour)


        actual =plate.get_driving_condition()
        expected_hour = '16:00'

        self.assertEqual(actual_plate, expected_plate)


if __name__ == '__main__':
    unittest.main()
