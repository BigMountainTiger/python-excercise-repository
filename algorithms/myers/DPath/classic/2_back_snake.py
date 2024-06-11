# https://blog.jcoglan.com/2017/03/22/myers-diff-in-linear-space-theory/

from utils import utilities

# 1. delta = width − height (N - M)
# 2. k = x - y
# 3. c = k - delta => c = x - y - delta


def backward(S):
    a = S['a']
    b = S['b']

    T = []

    N = len(a)
    M = len(b)
    MAX = N + M
    delta = N - M

    V = [None] * (MAX + 2)
    for D in range(0, MAX + 1):
        for k in range(-(D - 2*max(0, D-N)), D - 2*max(0, D-M) + 1, 2):

            if D == 0:
                x = N
            elif -k == D:
                x = V[k + 1] - 1
            elif k == D:
                x = V[k - 1]
            elif V[k - 1] < V[k + 1] - 1:
                x = V[k - 1]
            else:
                x = V[k + 1] - 1

            y = x - k - delta

            while x > 0 and y > 0 and a[x - 1] == b[y - 1]:
                x = x - 1
                y = y - 1

            V[k] = x

            if x == 0 and y == 0:
                T.append(V.copy())
                return T

        T.append(V.copy())


def forwardtrace(T, S):
    a = S['a']
    b = S['b']
    N = len(a)
    M = len(b)
    delta = N - M

    E = []

    # k = x - y - delta
    k = -delta
    D = len(T) - 1
    for d in range(D, 0, -1):
        t = T[d]

        if -k == d:
            next_k = k + 1
        elif k == d:
            next_k = k - 1
        elif t[k - 1] < t[k + 1] - 1:
            next_k = k - 1
        else:
            next_k = k + 1

        if next_k > k:
            edit = '-'
        else:
            edit = "+"

        next_x = t[next_k]
        next_y = next_x - next_k - delta
        k = next_k

        E.append({
            'e': edit,
            'x': next_x,
            'y': next_y,
            'payload': a[next_x - 1] if edit == '-' else b[next_y - 1]
        })

    return E


if __name__ == '__main__':

    S = {
        'a': 'BATD',
        'b': 'ABACD'
    }

    # S = {
    #     'a': 'GHFBATTTTD',
    #     'b': 'GHFABACD'
    # }

    print(S['a'])
    print(S['b'])

    T = backward(S)
    E = forwardtrace(T, S)

    print()
    print('b & rebuilt from a and E:')
    print(S['b'])
    b = utilities.build_b(S['a'], E)
    print(b)

    print()
    print('Print diff:')
    utilities.print_diff(S, E)
