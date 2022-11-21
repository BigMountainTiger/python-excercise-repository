import s3
import time

from datetime import datetime, timezone

class Utility(object):

    @staticmethod
    def is_empty(str_value: str) -> bool:
        return not bool(str_value and str_value.strip())

    @staticmethod
    def normalize(str_value: str, default=None):
        if str_value is None:
            return default

        if type(str_value) != str:
            return str_value

        return str_value.strip()

    @staticmethod
    def generate_timestamp_string(tz: timezone = timezone.utc, fmt: str = "%Y-%m-%dT%H:%M:%S") -> str:
        if tz is None:
            tz = timezone.utc

        if Utility.is_empty(fmt):
            fmt = "%Y-%m-%dT%H:%M:%S"

        return f'{datetime.now(tz).strftime(fmt)}'

    @staticmethod
    def epoch_time():
        return int(time.time()*1000)


def run():

    bucket = s3.Bucket('example.huge.head.li')

    # A valid file path
    key = 'AA/BB/File-A'
    exist = bucket.is_exist(key)
    print(exist)

    # A valid directory 
    key = 'AA/'
    exist = bucket.is_exist(key)
    print(exist)

    # A invalid file path
    key = None
    key = '//' if Utility.is_empty(key) else key
    exist = bucket.is_exist(key)
    print(exist)

    print('Validate string Not None or spaces')

    key = None
    print(Utility.is_empty(key))

    key = ''
    print(Utility.is_empty(key))

    key = ' '
    print(Utility.is_empty(key))

    key = 'A'
    print(Utility.is_empty(key))



if __name__ == '__main__':
    run()