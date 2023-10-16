from datetime import date, timedelta


def dates_generator(start_date, end_date):
    dates = start_date
    one_day = timedelta(days=1)
    while dates <= end_date:
        yield dates
        dates += one_day


if __name__ == "__main__":
    startDate = date(2025, 4, 27)
    endDate = date(2025, 5, 7)
    for date_between in dates_generator(startDate, endDate):
        print(date_between)
