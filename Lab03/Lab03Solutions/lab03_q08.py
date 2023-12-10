import datetime as d


def date_gen(start, end):
    print(start)
    while start != end:
        start += d.timedelta(days=1)
        yield start


start_date = d.date(2025, 4, 27)
end_date = d.date(2025, 5, 7)

for dates in date_gen(start_date, end_date):
    print(dates)
