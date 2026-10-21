import calendar
from datetime import date, datetime, timedelta
from dateutil.relativedelta import relativedelta

def get_calendar_mnt():
    now = datetime.now()
    return int(now.strftime('%Y%m'))


def get_previous_mnt(mnt):
    first_day_of_mnt = datetime.strptime(f'{mnt}01', '%Y%m%d')
    last_day_of_previous_mnt = first_day_of_mnt - timedelta(days=1)
    return int(last_day_of_previous_mnt.strftime('%Y%m'))


def get_next_mnt(mnt):
    first_day_of_mnt = datetime.strptime(f'{mnt}01', '%Y%m%d')
    first_day_of_next_mnt = first_day_of_mnt + relativedelta(months=1)
    return int(first_day_of_next_mnt.strftime('%Y%m'))


def get_mnt_by_offset(base_mnt, offset):
    first_day_of_mnt = datetime.strptime(f'{base_mnt}01', '%Y%m%d')
    first_day_of_offset_mnt = first_day_of_mnt + relativedelta(months=offset)
    return int(first_day_of_offset_mnt.strftime('%Y%m'))

def get_weekdays_of_month(mnt) -> list[date]:
    yr = int(str(mnt)[:4])
    mn = int(str(mnt)[4:])
    num_days = calendar.monthrange(yr,  mn)[1]

    weekdays = []
    for d in range(1, num_days + 1):
        current_date = date(yr, mn, d)
        if 0 <= current_date.weekday() <= 4:
            weekdays.append(current_date)

    return weekdays


if __name__ == "__main__":
    mnt = get_calendar_mnt()
    week_days = get_weekdays_of_month(mnt)
    for d in week_days:
        print(d)

