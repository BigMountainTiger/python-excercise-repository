import datetime
import time
from functools import lru_cache


@lru_cache(maxsize=1)
def cached_function():
    print('The cached_function() is called')

    now = datetime.datetime.now()
    return now


def run():
    print(cached_function)

    print()
    print(cached_function())
    print(cached_function())
    print(cached_function())

    print()
    print('Manually clear the cache')
    cached_function.cache_clear()
    print(cached_function())
    print(cached_function())
    print(cached_function())

    print()
    print('lru_cache is taking effect')


if __name__ == '__main__':
    run()
