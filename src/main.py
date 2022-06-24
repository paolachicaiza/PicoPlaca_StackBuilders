from src.parameters import second_start_shift, second_end_shift, first_start_shift, first_end_shift, pico_placa_day, \
    workdays, weekends
from src.utils import check_date, check_plate, time_in_range

date_str = '04-12-2018'
time_str = "19:23"
plate = "PDW-3264"

day = check_date(date_str)
last_digit = int(check_plate(plate))

print(last_digit, day, time_str)
days_circulate = pico_placa_day(day)
print(days_circulate)



first_circulate = time_in_range(first_start_shift, first_end_shift, time_str)
second_circulate = time_in_range(second_start_shift, second_end_shift, time_str)

if day in workdays:
    if last_digit in pico_placa_day(day):
        if first_circulate or second_circulate:
            print("No circula")
        else:
            print("Circula")
    else:
        print("Circula")
elif day in weekends:
    print("Circula")