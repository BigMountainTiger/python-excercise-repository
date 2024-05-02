# https://scipython.com/book2/chapter-6-numpy/examples/creating-a-magic-square/
import sys
import numpy as np

N = int(sys.argv[1])
magic_square = np.zeros((N, N), dtype=int)

n = 1
i, j = 0, N//2

while n <= N**2:
    magic_square[i, j] = n
    n += 1
    newi, newj = (i-1) % N, (j+1) % N
    if magic_square[newi, newj]:
        i += 1
    else:
        i, j = newi, newj

print(magic_square)
