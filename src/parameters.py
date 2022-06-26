workdays = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday"]
weekends = ["Saturday", "Sunday"]
holidays = ['01-01-2022','28-02-2022','01-03-2022','15-04-2022','02-05-2022','23-05-2022','10-08-2022','12-08-2022','09-10-2022','02-11-2022','03-11-2022','25-12-2022'
]

first_start_shift = "06:00"
first_end_shift = "09:30"
second_start_shift = "16:00"
second_end_shift = "21:00"

plates = [1, 2, 3, 4, 5, 6, 7, 8, 9, 0]


def forbidden_day(day):
    forbidden_day_plates = {}
    i = 0
    for workday in workdays:
        forbidden_day_plates[workday] = [plates[i], plates[i + 1]]
        i = i + 2
    return forbidden_day_plates[day]
