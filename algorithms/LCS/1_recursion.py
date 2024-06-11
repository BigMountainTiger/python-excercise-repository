a = 'BATD'
b = 'ABACD'


def lcs(a, la, b, lb):
    result = None

    if la == 0 or lb == 0:
        result = 0
    elif a[la - 1] == b[lb - 1]:
        result = 1 + lcs(a, la - 1, b, lb - 1)
    else:
        result = max(lcs(a, la - 1, b, lb), lcs(a, la, b, lb - 1))

    return result


def run():

    la = len(a)
    lb = len(b)

    count = lcs(a, la, b, lb)

    print(a)
    print(b)
    print(f'The longest common subsequence has length {count}')


if __name__ == '__main__':
    run()
