import datetime as dt

if __name__ == '__main__':

    now = dt.datetime.now()
    print(f'Default now() has no timezone information - {now}')

    print()
    utc_now = dt.datetime.now(dt.timezone.utc)
    print(f'UTC time - {utc_now}')

    print()
    print('datetime can be converted to another timezone')
    us_east = dt.timezone(dt.timedelta(hours=-5))
    us_east_now = utc_now.astimezone(us_east)
    print(f'us_east time - {us_east_now}')

    print()
    now = dt.datetime.now()
    us_east_tz = dt.timezone(dt.timedelta(hours=-5))
    us_east_now = now.astimezone(us_east_tz)

    print('Adding the timezone information to datetime without timezone dose not change its time part')
    print(now)
    print(us_east_now)
