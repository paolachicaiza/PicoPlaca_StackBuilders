workdays = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday"]
weekends = ["Saturday", "Sunday"]
hollydays = []

first_start_shift = "06:00"
first_end_shift = "09:30"
second_start_shift = "16:00"
second_end_shift = "21:00"

plates = [1, 2, 3, 4, 5, 6, 7, 8, 9, 0]


def pico_placa_day(day):
    pico_placa = {}
    i = 0
    plates_day = []
    for workday in workdays:
        pico_placa[workday] = [plates[i], plates[i + 1]]
        i = i + 2
        plates_day = []

    for weekend in weekends:
        pico_placa[weekend] = plates

    return pico_placa[day]
