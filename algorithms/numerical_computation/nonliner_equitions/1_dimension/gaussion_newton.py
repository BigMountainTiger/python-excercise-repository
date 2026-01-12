# solve x^2 = 1

import time

def prime(x):
  return 2*x

def error(x):
  return 0.5 * ((x**2 - 1)**2)

def solve():

  x = 0.01

  for i in range(100):

    delta = (1 - x**2) / prime(x)
    x = x + delta

  print(f'x={x} error={error(x)}')


if __name__ == '__main__':

  start_time = time.time()
  solve()

  print(f'{(time.time() - start_time) * 1000} ms')