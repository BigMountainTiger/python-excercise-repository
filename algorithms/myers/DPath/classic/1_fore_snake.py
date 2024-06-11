# https://blog.jcoglan.com/2017/02/17/the-myers-diff-algorithm-part-3/

from utils import utilities


def forward(S):
    a = S['a']
    b = S['b']

    T = []

    N = len(a)
    M = len(b)
    MAX = N + M

    V = [None] * (MAX + 2)
    V[1] = 0
    for D in range(0, MAX + 1):
        for k in range(-(D - 2*max(0, D-M)), D - 2*max(0, D-N) + 1, 2):

            if k == -D or k != D and V[k - 1] < V[k + 1]:
                x = V[k + 1]
            else:
                x = V[k - 1] + 1
            y = x - k

            while x < N and y < M and a[x] == b[y]:
                x = x + 1
                y = y + 1

            V[k] = x

            if x == N and y == M:
                T.append(V.copy())
                return T

        T.append(V.copy())


def backtrace(T, S):
    a = S['a']
    b = S['b']
    k = len(a) - len(b)

    E = []

    D = len(T) - 1
    for d in range(D, 0, -1):
        t = T[d]

        if k == -d or (k != d and t[k - 1] < t[k + 1]):
            edit = "+"
            prev_k = k + 1
        else:
            edit = '-'
            prev_k = k - 1

        prev_x = t[prev_k]
        prev_y = prev_x - prev_k
        k = prev_k

        E.append({
            'e': edit,
            'x': prev_x + 1 if edit == '-' else prev_x,
            'y': prev_y + 1 if edit == '+' else prev_y,
            'payload': a[prev_x] if edit == '-' else b[prev_y]
        })

    return E[::-1]


if __name__ == '__main__':

    S = {
        'a': 'GHFBATTTTD',
        'b': 'GHFABACD'
    }

    T = forward(S)
    E = backtrace(T, S)

    print('a:')
    print(S['a'])

    print()
    print('b & rebuilt from a and E:')
    print(S['b'])
    b = utilities.build_b(S['a'], E)
    print(b)

    print()
    print('Print diff:')
    utilities.print_diff(S, E)
