# https://docs.python.org/3/library/datetime.html#strftime-strptime-behavior

import datetime

if __name__ == '__main__':

    utc_now = datetime.datetime.now(datetime.timezone.utc)

    y = utc_now.strftime('%Y')
    m = utc_now.strftime('%m')
    d = utc_now.strftime('%d')
    h = utc_now.strftime('%H')
    min = utc_now.strftime('%M')
    s = utc_now.strftime('%S')
    f = utc_now.strftime('%f')
    z = utc_now.strftime('%z')

    print('Basic usage')
    print(f'year = {y}')
    print(f'month = {m}')
    print(f'day = {d}')
    print(f'hour = {h}')
    print(f'minute = {min}')
    print(f'second = {s}')
    print(f'microsecond = {f}')
    print(f'timezone = {z}')

    print()
    now = datetime.datetime.now()
    z = now.strftime('%z')
    # If the datetime has no timezone information, it is empty by '%z'
    print(f'datetime without timezone = {'empty string' if z == '' else z}')

