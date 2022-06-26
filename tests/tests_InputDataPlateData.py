import unittest

from src.input_reader import InputReader


class MyTestCase(unittest.TestCase):
    def test_read_data(self):
        input_data = InputReader()
        input_data.read_data("data.txt")
        actual = input_data.lines
        self.assertTrue(len(actual) > 0)

    def test_parse_lines(self):
        input_data = InputReader()
        input_data.read_data("data.txt")
        input_data.parse_lines()
        actual = input_data.cars
        print(actual)


if __name__ == '__main__':
    unittest.main()





