from datetime import datetime


def check_date(date_str):
    date_checker = datetime.strptime(date_str, '%d-%m-%Y').date()
    return date_checker.strftime("%A")


def check_plate(plate):
    return plate[-1]


def time_in_range(start, end, hour_checker):
    start_obj = datetime.strptime(start, '%H:%M')
    end_obj = datetime.strptime(end, '%H:%M')
    hour_checker_obj = datetime.strptime(hour_checker, '%H:%M')

    return start_obj <= hour_checker_obj <= end_obj
