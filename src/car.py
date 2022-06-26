from src.vehicle import Vehicle


class Car(Vehicle):

    def __init__(self, plate):
        super().__init__(plate)

    def get_digit_checker(self):
        return int(self.plate[-1])
