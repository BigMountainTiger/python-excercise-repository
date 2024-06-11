# https://blog.robertelder.org/diff-algorithm/

# length of V = MAX * 2
def SEL_length(old, new):
    N = len(old)
    M = len(new)
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

            while x < N and y < M and old[x] == new[y]:
                x = x + 1
                y = y + 1

            V[k] = x

            if x == N and y == M:
                return D


if __name__ == '__main__':

    a = 'BATD'
    b = 'ABACD'

    D = SEL_length(a, b)
    print(D)
