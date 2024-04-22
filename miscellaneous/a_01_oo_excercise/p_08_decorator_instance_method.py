from functools import wraps


def my_decorator(func):

    ct = 0

    @wraps(func)
    def wrapper(*args, **kwargs):
        # This is the nonlocal variable
        nonlocal ct

        ct += 1
        return ct

    return wrapper

class my_class():
    def __init__(self):
        pass

    @my_decorator
    def instance_method(self):
        pass

if __name__ == '__main__':
    
    o1 = my_class()
    o2 = my_class()

    print('The annotated method has a global state')
    print(o1.instance_method())
    print(o2.instance_method())

    print()
    print('https://stackoverflow.com/questions/51542063/decorators-for-instance-methods')
    print('The order of operation:')
    print('1. When the my_decorator() decorator is called, instance_method() is not a method yet, it is still a function')
    print('2. It is only when the class block is over that instance_method is transformed into a method by the metaclass descriptors')