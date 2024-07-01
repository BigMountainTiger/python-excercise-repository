import random


def quick_sort(d, n=None, m=None):
    n = 0 if n is None else n
    m = len(d) - 1 if m is None else m

    size = m - n + 1
    if size == 1:
        pass
    elif size == 2:
        if d[n] > d[m]:
            d[n], d[m] = d[m], d[n]
    else:
        mid = n + size // 2 - 1
        quick_sort(d, n, mid)
        quick_sort(d, mid + 1, m)

        i = n
        l, li, l_last = d[n:mid + 1], 0, mid - n
        r, ri, r_last = d[mid + 1:m + 1], 0, m - mid - 1

        while li <= l_last or ri <= r_last:
            if l[li] < r[ri]:
                d[i], li, i = l[li], li + 1, i + 1
                if li > l_last:
                    while ri <= r_last:
                        d[i], ri, i = r[ri], ri + 1, i + 1
            else:
                d[i], ri, i = r[ri], ri + 1, i + 1
                if ri > r_last:
                    while li <= l_last:
                        d[i], li, i = l[li], li + 1, i + 1


if __name__ == '__main__':

    # d has duplicates
    L = range(50)
    d = [random.choice(L) for _ in range(10)] * 2

    quick_sort(d)
    print(d)
