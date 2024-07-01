import random
import string
from utils import utilities
from linear_myers import diff


def test(a, b):
    E = diff(a, b)
    # resuld b by a and E to compare with the original b
    bb = utilities.build_b(a, E)
    if (b != bb):
        print(a)
        print(b)
        print(bb)
        raise "The recreated b does not match the original"


if __name__ == '__main__':

    # 1. Edge cases
    test('', '')
    test('', 'ABCDEFGHIJK')
    test('ABCDEFGHIJK', '')

    # 2. a = b
    n = 100
    test('A' * n, 'A' * n)
    test('A' * (n + 1), 'A' * (n + 1))

    # 3. Totally different
    n = 100
    test('A' * n, 'B' * n)
    test('A' * (n + 1), 'B' * n)
    test('A' * (n + 2), 'B' * n)
    test('A' * n, 'B' * (n + 1))
    test('A' * n, 'B' * (n + 2))

    # 4. power test by random strings
    for _ in range(100):
        # delta = N -M = 0
        a = ''.join(random.choices(string.ascii_uppercase, k=100))
        b = ''.join(random.choices(string.ascii_uppercase, k=100))
        test(a, b)

    for _ in range(100):
        # even
        a = ''.join(random.choices(string.ascii_uppercase, k=100))
        b = ''.join(random.choices(string.ascii_uppercase, k=200))
        test(a, b)

        # odd
        a = ''.join(random.choices(string.ascii_uppercase, k=100))
        b = ''.join(random.choices(string.ascii_uppercase, k=201))
        test(a, b)

    for _ in range(100):
        # even
        a = ''.join(random.choices(string.ascii_uppercase, k=200))
        b = ''.join(random.choices(string.ascii_uppercase, k=100))
        test(a, b)

        # odd
        a = ''.join(random.choices(string.ascii_uppercase, k=200))
        b = ''.join(random.choices(string.ascii_uppercase, k=99))
        test(a, b)

    print('Success')
