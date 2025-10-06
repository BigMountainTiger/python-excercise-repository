import copy


def example():
    A = {
        'V': []
    }

    B = copy.deepcopy(A)
    B['V'].append(1)
    print(A)


if __name__ == '__main__':
    example()

    print()
    print('1. The copy.deepcopy() can create a deep copy of an object')
    print('2. A deep copy constructs a new compound object and then, recursively, inserts copies into it of the objects found in the original')
