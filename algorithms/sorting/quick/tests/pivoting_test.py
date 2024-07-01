import random
from utils import utilities


def pivoting(d, n=None, m=None):
    n = 0 if n is None else n
    m = len(d) - 1 if m is None else m

    pivot = d[m]
    li, ri = n, m - 1

    # Equal sign is required ...
    # so the list is sorted even only 2 entries in the list
    while li <= ri:
        # Get the first index from left that > pivot
        while d[li] <= pivot and li <= m - 1:
            li = li + 1

        # Get the first index from right that < pivot
        while d[ri] >= pivot and ri >= n:
            ri = ri - 1

        if li < ri:
            d[li], d[ri] = d[ri], d[li]

    pi = li
    d[pi], d[m] = d[m], d[pi]

    return pi


if __name__ == '__main__':

    d = [1, 0]

    print(d)

    n = 0
    m = len(d) - 1
    pi = pivoting(d)

    print('------------------')
    print(f'pi = {pi}')
    print(f'({n}, {pi - 1}) - {pi} - ({pi + 1}, {m})')

    print(d)
