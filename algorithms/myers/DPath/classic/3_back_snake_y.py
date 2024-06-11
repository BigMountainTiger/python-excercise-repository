# https://blog.jcoglan.com/2017/04/25/myers-diff-in-linear-space-implementation/
# This save the y values in the V array

from utils import utilities


def backward(S):
    a = S['a']
    b = S['b']

    T = []

    N = len(a)
    M = len(b)
    MAX = N + M
    delta = N - M

    V = [None] * (MAX + 2)
    V[1] = M
    for D in range(0, MAX + 1):
        for c in range(-(D - 2*max(0, D-N)), D - 2*max(0, D-M) + 1, 2):

            if c == -D or (c != D and V[c - 1] > V[c + 1]):
                y = V[c + 1]
            else:
                y = V[c - 1] - 1

            x = y + (c + delta)

            while x > 0 and y > 0 and a[x - 1] == b[y - 1]:
                x, y = x - 1, y - 1

            V[c] = y

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

    # c = x - y - delta
    c = -delta
    D = len(T) - 1
    for d in range(D, 0, -1):
        t = T[d]

        if c == -d or (c != d and t[c - 1] > t[c + 1]):
            edit = "-"
            next_c = c + 1
        else:
            edit = '+'
            next_c = c - 1

        next_y = t[next_c]
        next_x = next_y + next_c + delta
        c = next_c

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
