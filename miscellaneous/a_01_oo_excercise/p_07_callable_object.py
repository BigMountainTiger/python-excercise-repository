from typing import Any


class A():
    def __init__(self, param):
        self.param = param

    def __call__(self):
        print(f'Printed from the __call__() method - {self.param}')


def run():
    print()
    A('OK')()


if __name__ == '__main__':
    run()
