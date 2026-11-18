# Need pip install holidays
from datetime import date, timedelta
import holidays


def list_holidays():
    us_holidays = holidays.US(years=2027)

    for date, name in sorted(us_holidays.items()):
        print(f"{date}: {name}")


def check_if_holiday(day):
    us_holidays = holidays.US()
    if day in us_holidays:
        print(f"{day} is a holiday: {us_holidays[day]}")
        return True

    return False

def dates_in_year(year):
    current_date = date(year, 1, 1)
    end_date = date(year + 1, 1, 1)
    
    while current_date < end_date:
        yield current_date
        current_date += timedelta(days=1)

ct = 0
for d in dates_in_year(2026):
    if check_if_holiday(d):
        ct += 1
print(f"Total holidays: {ct}")

print()
ct = 0
for d in dates_in_year(2027):
    if check_if_holiday(d):
        ct += 1
print(f"Total holidays: {ct}")

print()
ct = 0
for d in dates_in_year(2028):
    if check_if_holiday(d):
        ct += 1
print(f"Total holidays: {ct}")