import copy


def example():
    A = 1
    B = copy.copy(A)

    print(f'A = {A}, B = {B}')


if __name__ == '__main__':
    example()

    print()
    print('Copy can be used for any objects, including immutable ones')
