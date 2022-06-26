from src.parameters import weekends, holidays, forbidden_day
from src.utils import get_day_name, get_last_digit_plate, is_forbidden_time


class Validator:
    def __init__(self, vehicle, raw_date, raw_hour):
        self.vehicle = vehicle
        self.raw_date = raw_date
        self.raw_hour = raw_hour
        self.day = get_day_name(self.raw_date)

    def is_weekend_or_holiday(self):
        return self.day in weekends or self.raw_date in holidays

    def is_driving_allowed(self):
        """
        :return True: circulate
        :return False: no circulate
        """
        last_digit = get_last_digit_plate(self.vehicle.plate)

        if self.is_weekend_or_holiday():
            return True

        if last_digit in forbidden_day(self.day):
            if is_forbidden_time(self.raw_hour):
                return False

        return True
