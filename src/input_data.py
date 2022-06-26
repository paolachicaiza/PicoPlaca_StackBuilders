class InputData:
    def __init__(self, raw_plate, raw_date, raw_hour):
        self.raw_plate = raw_plate
        self.raw_date = raw_date
        self.raw_hour = raw_hour


    def get_raw_plate(self):
        return self.raw_plate

    def get_raw_date(self):
        return self.raw_date

    def get_raw_hour(self):
        return self.raw_hour
