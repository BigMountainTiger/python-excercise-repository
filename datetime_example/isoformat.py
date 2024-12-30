# https://docs.python.org/3/library/datetime.html#datetime.date.fromisoformat

import datetime

if __name__ == '__main__':

    utc_now = datetime.datetime.now(datetime.timezone.utc)

    print('ISO string from datetime')
    iso_string = utc_now.isoformat()
    print(iso_string)

    print()
    print('datetime from ISO string')
    utc_now = datetime.datetime.fromisoformat(iso_string)
    print(utc_now)

    print()
    now = datetime.datetime.now()
    print('ISO string from datetime without timezone has not timezone information')
    iso_string = now.isoformat()
    print(iso_string)
