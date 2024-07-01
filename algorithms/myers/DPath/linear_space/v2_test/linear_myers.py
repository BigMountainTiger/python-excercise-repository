from utils import utilities


def mid_snake(a, b):
    N, M = len(a), len(b)
    MAX, delta = N + M, N - M
    left, top, right, bottom, even = 0, 0, N, M, delta % 2 == 0

    VF, VB = [None] * (MAX + 2), [None] * (MAX + 2)
    VF[1], VB[1] = left, bottom

    for D in range(0, MAX + 1):
        # forward
        for k in range(D - 2*max(left, D-right), -(D - 2*max(top, D-bottom)) - 1,  -2):
            cc = k - delta

            if k == -D or (k != D and VF[k - 1] < VF[k + 1]):
                px = x = VF[k + 1]
            else:
                px = VF[k - 1]
                x = px + 1

            y = top + (x - left) - k
            py = y if (D == 0 or x != px) else y - 1

            while x < right and y < bottom and a[x] == b[y]:
                x, y = x + 1, y + 1
            VF[k] = x

            if not even and -(D - 1) <= cc <= (D - 1) and y >= VB[cc]:
                return ((px, py), (x, y), 2*D - 1)

        # backward
        for c in range(D - 2*max(top, D-bottom), -(D - 2*max(left, D-right)) - 1, -2):
            kk = c + delta

            if c == -D or (c != D and VB[c - 1] > VB[c + 1]):
                py = y = VB[c + 1]
            else:
                py = VB[c - 1]
                y = py - 1

            x = left + (y - top) + kk
            px = x if (D == 0 or y != py) else x + 1

            while x > left and y > top and a[x - 1] == b[y - 1]:
                x, y = x - 1, y - 1
            VB[c] = y

            if even and -D <= kk <= D and x <= VF[kk]:
                return ((x, y), (px, py), 2*D)


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
