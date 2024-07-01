import random


def bubble_sort(d):
    n = len(d)

    for i in range(n - 1):
        swapped = False
        for j in range(n - i - 1):
            if d[j] > d[j + 1]:
                d[j], d[j+1] = d[j + 1], d[j]
                swapped = True

        if not swapped:
            break

    return d


if __name__ == '__main__':

    # d has duplicates
    L = range(10)
    d = [random.choice(L) for _ in range(10)] * 2

    d = bubble_sort(d)
    print(d)
