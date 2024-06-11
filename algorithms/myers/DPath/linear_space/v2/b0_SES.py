from utils import utilities
from a0_mid_snake import mid_snake


def diff(a, b, x0=0, y0=0):
    N, M = len(a), len(b)

    E = []
    if N == 0 and M == 0:
        return E

    if M == 0 and N > 0:
        for x in range(N):
            E.append(utilities.edit('-', x0 + x + 1, y0, a[x]))

        return E

    if N == 0 and M > 0:
        for y in range(M):
            E.append(utilities.edit('+', x0, y0 + y + 1, b[y]))

        return E

    s = mid_snake(a, b)
    x, y, u, v, D = s[0][0], s[0][1], s[1][0], s[1][1], s[2]
    x1, y1, u1, v1 = x0 + x, y0 + y, x0 + u, y0 + v
    even = D % 2 == 0

    if D == 0:
        return []
    elif D == 1:
        if (v - y) > (u - x):
            E.append(utilities.edit('+', x1, y1 + 1, b[y]))
        else:
            E.append(utilities.edit('-', x1 + 1, y1, a[x]))

        return E
    else:
        add = (v - y) > (u - x)
        if not even:
            if add:
                E.append(utilities.edit('+', x1, y1 + 1, b[y]))
            else:
                E.append(utilities.edit('-', x1 + 1, y1, a[x]))
        else:
            if add:
                E.append(utilities.edit('+', u1, v1, b[v - 1]))
            else:
                E.append(utilities.edit('-', u1, v1, a[u - 1]))

        EL = diff(a[0:x], b[0:y], x0, y0)
        ER = diff(a[u:], b[v:], u1, v1)

        return EL + E + ER


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

    print()
    E = diff(S['a'], S['b'])
    print('a:')
    print(S['a'])

    print()
    print('b & rebuilt from a and E:')
    print(S['b'])
    b = utilities.build_b(S['a'], E)
    print(b)

    utilities.print_diff(S, E)
