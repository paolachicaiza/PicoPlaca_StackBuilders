from src.car import Car
from src.parser import Parser
from src.validator import Validator

filename = "data.txt"
parser = Parser(filename)
parser.read_data()

for data in parser.parsed_data:
    vehicle = Car(data.get_raw_plate())
    raw_date = data.get_raw_date()
    raw_hour = data.get_raw_hour()
    validator = Validator(vehicle, raw_date, raw_hour)
    circulation_allowed = validator.is_driving_allowed()
    if circulation_allowed:
        print(f"{vehicle.plate}: Driving allowed")
    else:
        print(f"{vehicle.plate}: Driving NOT allowed")
