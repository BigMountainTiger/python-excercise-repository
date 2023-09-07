from functools import update_wrapper, wraps
from datetime import datetime, timedelta
import time


class decorator_0():

    def __init__(self, func):
        self.func = func
        update_wrapper(self, func)

    def __call__(self, *args, **kwargs):
        return f'Decorated - {self.func(*args, **kwargs)}'

    def additional_method(self):
        return 'Class decorator can add additonal methods'


@decorator_0
def func_0():
    return 'func_0 data'


class decorator_1():

    def __init__(self, expires):
        self.expires = expires
        self.cache = {}

    def __call__(self, func):
        cache = self.cache
        expires = self.expires

        @wraps(func)
        def wrapper(*args, **kwargs):
            result = cache.get('result')
            cached = cache.get('cached') or datetime.min

            if (result is not None) and ((cached + timedelta(seconds=expires)) > datetime.now()):
                return result

            result = func(*args, **kwargs)

            cache['result'] = result
            cache['cached'] = datetime.now()

            return result

        return wrapper


@decorator_1(expires=5)
def func_1():
    now = datetime.now()
    return now


def run():
    print('0. A basic class decorator example')
    print(func_0())
    print(func_0.additional_method())

    print()
    print('A cache decorator with parameters - expires in seconds')
    print(func_1())
    print(func_1())
    time.sleep(5)
    print('Sleep for 5 seconds')
    print(func_1())
    print(func_1())


if __name__ == '__main__':
    run()
