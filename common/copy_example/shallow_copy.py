import copy


def example_1():
    A = {
        'V': []
    }

    B = A.copy()
    B['V'].append(1)
    print(A)


def example_2():
    A = {
        'V': []
    }

    B = copy.copy(A)
    B['V'].append(1)
    print(A)


if __name__ == '__main__':
    example_1()
    example_2()

    print()
    print('1. Multiple ways to make copies')
    print('2. With shallow copies, all the copies share the same internal mutable objects')
    print('3. If any mutable objects are altered, all the copies are altered')

    print()
    print('A shallow copy constructs a new compound object and then (to the extent possible) inserts references into it to the objects found in the original')
