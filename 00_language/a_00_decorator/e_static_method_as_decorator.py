from functools import wraps


class example_class():
    @staticmethod
    def __tripple(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            for _ in range(3):
                func(*args, **kwargs)

        return wrapper

    # The __init__
    def __init__(self):
        self.value = 0

    @__tripple
    def increment(self):
        self.value += 1

    @property
    def current_value(self):
        return self.value


if __name__ == '__main__':
    o = example_class()
    print(f'initial value = {o.current_value}')

    o.increment()
    print(f'current value = {o.current_value}')

    print()
    print('Conclusion')
    print('If a private decorator is needed, a private @staticmethod is a good choice')
