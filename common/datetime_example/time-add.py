# https://docs.python.org/3/library/datetime.html#datetime.date.fromisoformat

import datetime

if __name__ == '__main__':

    utc_now = datetime.datetime.now(datetime.timezone.utc)
    print(f'original time')
    print(f'{utc_now}')

    print()
    print('Add an hour')
    t = utc_now + datetime.timedelta(hours=1)
    print(f'{t}')
