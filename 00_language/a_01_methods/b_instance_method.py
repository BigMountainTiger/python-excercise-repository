from functools import lru_cache
from functools import wraps


def decorator_1(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        func(*args, **kwargs)

    return wrapper

class example_class():
    def __init__(self, name):
        self.name = name

    @decorator_1
    def method_1(self):
        print(f'Print from {self.name}')


if __name__ == '__main__':

    print('The id of the instance method mostly the same')
    print('but can be different some times')
    o1 = example_class('instance 1')
    o2 = example_class('instance 2')

    print(id(o1.method_1))
    print(id(o2.method_1))

    print()
    o1.method_1()
    o2.method_1()
    print(id(o1.method_1))
    print(id(o2.method_1))