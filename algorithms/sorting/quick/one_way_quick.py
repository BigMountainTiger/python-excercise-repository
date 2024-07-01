# https://www.w3schools.com/dsa/dsa_algo_quicksort.php

import random
from utils import utilities


def quick_sort(d, n=None, m=None):
    n = 0 if n is None else n
    m = len(d) - 1 if m is None else m

    if n < m:
        pivot = d[m]

        pi = n - 1
        # pi + 1 for any entry <= the pivot
        for i in range(n, m):
            if d[i] <= pivot:
                pi = pi + 1
                d[i], d[pi] = d[pi], d[i]

        pi = pi + 1
        d[pi], d[m] = d[m], d[pi]

        quick_sort(d, n, pi - 1)
        quick_sort(d, pi + 1, m)


if __name__ == '__main__':

    # d has duplicates
    L = range(50)
    d = [random.choice(L) for _ in range(10)] * 2

    quick_sort(d)
    print(d)

    utilities.validate_sorted(d)
