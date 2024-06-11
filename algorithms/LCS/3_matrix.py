a = 'BATD'
b = 'ABACD'


def lcs(a, b):
    matrix = []
    for i in range(len(b)):

        row = []
        matrix.append(row)
        for j in range(len(a)):
            v = None
            if b[i] == a[j]:
                v = 1 + (0 if i == 0 or j == 0 else matrix[i - 1][j - 1])
            else:
                v = max(0 if i == 0 else matrix[i - 1]
                        [j], 0 if j == 0 else matrix[i][j - 1])

            row.append(v)

    return matrix[len(b) - 1][len(a) - 1]


def run():
    count = lcs(a, b)

    print(a)
    print(b)
    print(f'The longest common subsequence has length {count}')


if __name__ == '__main__':
    run()
