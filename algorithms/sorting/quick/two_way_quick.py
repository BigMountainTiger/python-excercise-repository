import random
from utils import utilities


def quick_sort(d, n=None, m=None):
    n = 0 if n is None else n
    m = len(d) - 1 if m is None else m

    if n < m:
        pivot = d[m]

        li, ri = n, m - 1
        while li <= ri:
            while d[li] <= pivot and li <= m - 1:
                li = li + 1

            while d[ri] >= pivot and ri >= n:
                ri = ri - 1

            if li < ri:
                d[li], d[ri] = d[ri], d[li]

        pi = li
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
