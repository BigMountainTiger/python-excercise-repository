# https://docs.python.org/3/library/itertools.html

import itertools


def single_array_example():
    A = [[1, 2]]
    for i in itertools.product(*A):
        print(i)


def multi_array_example():
    A = [[1, 2], [1, 2]]
    for i in itertools.product(*A):
        print(i)


if __name__ == '__main__':

    print('single_array_example')
    single_array_example()

    print()
    print('multi_array_example')
    multi_array_example()
