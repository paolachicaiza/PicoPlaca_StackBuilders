from src.parameters import weekends, holidays, forbidden_day
from src.utils import get_day_name, get_last_digit_plate, forbidden_time


class DrivingConditionValidator:

    def __init__(self, plate_str, date_str, time_str):
        self.plate_str = plate_str
        self.date_str = date_str
        self.time_str = time_str
        self.message = str

    def get_driving_no_restrictions(self):
        day = get_day_name(self.date_str)
        return day in weekends or self.date_str in holidays

    def get_driving_condition(self):
        day = get_day_name(self.date_str)
        last_digit = get_last_digit_plate(self.plate_str)

        if self.get_driving_no_restrictions():
            self.message = "Circula"
            return
        else:
            if last_digit in forbidden_day(day):
                if forbidden_time(self.time_str):
                    self.message = "No Circula"
                    return
                self.message = "Circula"
                return
            self.message = "Circula"
            return

    def print_driving_condition(self):
        print(self.message)
