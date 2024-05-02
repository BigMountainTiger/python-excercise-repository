from functools import update_wrapper, wraps
from datetime import datetime, timedelta
import time



class decorator_0():

    def __init__(self, expires):
        self.expires = expires

    def __call__(self, func):
        pass
        


@decorator_0(expires=5)
def func_0():
    now = datetime.now()
    return now


def run():
    print(func_0)


if __name__ == '__main__':
    run()
