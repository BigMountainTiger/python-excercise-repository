from functools import wraps
from datetime import datetime, timedelta
import time

text = 'OK'


def decorator_0(func):
    return text


@decorator_0
def func_0():
    return 'func_1 data'


def decorator_1(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        func_result = func(*args, **kwargs)
        return f'The result is {func_result}'

    return wrapper


@decorator_1
def func_1(p1, p2):
    return f'p1={p1}, p2={p2}'


def decorator_2(func):
    state = {}
    key = 'call_count'

    @wraps(func)
    def wrapper(*args, **kwargs):

        state[key] = state.get(key, 0) + 1
        func_result = func(*args, **kwargs)
        return f'The {state.get(key)} time calling function {func_result}'

    return wrapper


@decorator_2
def func_2():
    return 'func_2'


def decorator_3(expires):
    # Decorator with parameters
    def decorator(func):

        cache = {}

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

    return decorator


@decorator_3(expires=5)
def func_3():
    now = datetime.now()
    return now


def run():
    print('A decorator can return anything')
    print(f'0. A decortator can return anything = {func_0 is text}')

    print()
    print('A normal decorator')
    print(f'1. A call from a normal decorated function -> {func_1(1, 2)}')

    print()
    print('A decorator can have state')
    print(f'2. A decorated function can keep the state -> {func_2()}')
    print(f'2. A decorated function can keep the state -> {func_2()}')
    print(f'2. A decorated function can keep the state -> {func_2()}')

    print()
    print('A decorator can have parameters')
    print(func_3())
    print(func_3())
    time.sleep(5)
    print('Sleep for 5 seconds')
    print(func_3())


if __name__ == '__main__':
    run()
