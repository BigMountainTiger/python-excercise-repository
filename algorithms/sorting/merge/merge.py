import random
from utils import utilities


def merge_sort(d, n=None, m=None):
    n = 0 if n is None else n
    m = len(d) - 1 if m is None else m

    size = m - n + 1
    if size == 1:
        pass
    elif size == 2:
        if d[n] > d[m]:
            d[n], d[m] = d[m], d[n]
    elif size == 3:
        i0, i1, i2 = n, n + 1, n + 2

        if d[i1] > d[i2]:
            d[i1], d[i2] = d[i2], d[i1]

        if d[i0] > d[i1]:
            d[i0], d[i1] = d[i1], d[i0]
            if d[i1] > d[i2]:
                d[i1], d[i2] = d[i2], d[i1]
    else:
        # size needs >= 2 so mid is not smaller than n
        mid = n + size // 2 - 1
        merge_sort(d, n, mid)
        merge_sort(d, mid + 1, m)

        i = n
        l, li, l_last = d[n:mid + 1], 0, mid - n
        r, ri, r_last = d[mid + 1:m + 1], 0, m - mid - 1

        # Both l & r are already sorted
        while li <= l_last and ri <= r_last:
            # The '<=' guranttees sorting stability
            if l[li] <= r[ri]:
                d[i], li, i = l[li], li + 1, i + 1
            else:
                d[i], ri, i = r[ri], ri + 1, i + 1

        # handle any leftovers if exist
        while ri <= r_last:
            d[i], ri, i = r[ri], ri + 1, i + 1
        while li <= l_last:
            d[i], li, i = l[li], li + 1, i + 1


if __name__ == '__main__':

    # d has duplicates
    L = range(50)
    d = [random.choice(L) for _ in range(10)] * 2

    merge_sort(d)
    print(d)

    utilities.validate_sorted(d)
