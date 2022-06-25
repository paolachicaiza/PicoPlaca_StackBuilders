from src.input_reader import InputReader
from src.driving_condition_validator import DrivingConditionValidator

if __name__ == "__main__":
    input_data = InputReader()
    input_data.read_data("test_data.txt")
    input_data.parse_lines()
    cars = input_data.cars
    print(cars)

    for car in cars:
        car_checked = DrivingConditionValidator(cars[car][0], cars[car][1], cars[car][2])
        car_checked.get_driving_condition()
        data_car = input_data.cars[car]
        car_checked.print_driving_condition()




