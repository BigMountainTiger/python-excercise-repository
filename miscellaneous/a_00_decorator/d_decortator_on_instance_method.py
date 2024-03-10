from functools import lru_cache


class example_class():
    def __init__(self, start):
        self.count = start

    @lru_cache(maxsize=128)
    def next(self):
        print('Method is called')
        self.count += 1
        return self.count


if __name__ == '__main__':

    o1 = example_class(0)
    o2 = example_class(0)

    print(o1.next())
    print(o1.next())

    print()
    print(o2.next())
    print(o2.next())

    print()
    print('It looks like two instances are using the same cache')
    print(o1.next.cache_info())
    print(o2.next.cache_info())

    print()
    print('Clear the cache by the reference on o1, the cache on o2 is cleared')
    o1.next.cache_clear()
    print(o2.next())
    print(o1.next.cache_info())
    print(o2.next.cache_info())

    print()
    print('From the observation it is OK to use lru_cache')
    print('But it should be noted that all the instances share the same cache')
    print('Because the "self" reference is different, so there is no conflict')