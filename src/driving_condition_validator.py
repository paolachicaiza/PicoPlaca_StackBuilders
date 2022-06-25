from src.parameters import weekends, holidays, forbidden_day
from src.utils import get_day_name, get_last_digit_plate, forbidden_time


class ValidationPlate:

    def __init__(self,plate_str, date_str, time_str):
        self.plate_str = plate_str
        self.date_str = date_str
        self.time_str = time_str
        self.validation = str

    def get_driving_condition(self):
        day = get_day_name(self.date_str)
        last_digit = get_last_digit_plate(self.plate_str)

        if day in weekends:
            msg = "Circula"
            self.validation = msg

        if self.date_str in holidays:
            msg = "Circula"
            self.validation = msg

        if last_digit in forbidden_day(day):
            if forbidden_time(self.time_str):
                msg = "No Circula"
                self.validation = msg
            msg = "Circula"
            self.validation = msg

        msg = "Circula"
        self.validation = msg

    def print_driving_condition(self):
        print(self.validation)