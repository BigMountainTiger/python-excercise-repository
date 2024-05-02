import datetime, time
from cachetools import cached, TTLCache

cache = TTLCache(maxsize= 1, ttl = 10)
@cached(cache=cache)
def cached_function():
    print('The cached_function() is called')

    now = datetime.datetime.now()
    return now

def run():
    
    print(cached_function())
    print(cached_function())
    print(cached_function())

    sleep_time = 5

    print()
    time.sleep(sleep_time)
    print(f'After {sleep_time} seconds')
    print(cached_function())
    print(cached_function())
    print(cached_function())

    print()
    time.sleep(sleep_time)
    print(f'After {sleep_time} seconds')
    print(cached_function())
    print(cached_function())
    print(cached_function())
    
    print()
    print('Manually clear the cache')
    cache.clear()
    print(cached_function())
    print(cached_function())
    print(cached_function())

    print()
    print('TTLCache is taking effect')

if __name__ == '__main__':
    run()