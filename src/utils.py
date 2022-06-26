from datetime import datetime

from src.parameters import first_start_shift, first_end_shift, second_start_shift, second_end_shift


def get_day_name(date_str):
    date_checker = datetime.strptime(date_str, '%d-%m-%Y').date()
    return date_checker.strftime("%A")


def is_time_in_range(start_1, end_1, start_2, end_2, hour_checker):
    start_obj_1 = datetime.strptime(start_1, '%H:%M')
    end_obj_1 = datetime.strptime(end_1, '%H:%M')

    start_obj_2 = datetime.strptime(start_2, '%H:%M')
    end_obj_2 = datetime.strptime(end_2, '%H:%M')

    hour_checker_obj = datetime.strptime(hour_checker, '%H:%M')

    is_time_in_range_1 = start_obj_1 <= hour_checker_obj <= end_obj_1
    is_time_in_range_2 = start_obj_2 <= hour_checker_obj <= end_obj_2

    return is_time_in_range_1 or is_time_in_range_2


def is_forbidden_time(hour_checker):
    return is_time_in_range(first_start_shift, first_end_shift,second_start_shift, second_end_shift, hour_checker)



