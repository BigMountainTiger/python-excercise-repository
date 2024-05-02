from itertools import permutations
import numpy as np


def verify(A):
    B = np.rot90(A)
    sum = np.sum(A[0])

    for i in range(0, A.shape[0]):
        if sum != np.sum(A[i]) or sum != np.sum(B[i]):
            return False

    if sum != np.trace(A) or sum != np.trace(B):
        return False

    return True


def huan_fang(dim):
    for s in permutations(range(1, dim * dim + 1)):
        A = np.array(s).reshape((dim, dim))
        if (verify(A)):
            return A


if __name__ == '__main__':

    dim = 4
    A = huan_fang(dim)

    print(A)
