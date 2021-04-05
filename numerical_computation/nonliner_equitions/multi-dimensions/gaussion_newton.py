# An example from Wikipedia
# https://en.wikipedia.org/wiki/Gradient_descent

import time
import math;
import numpy as np

def G(x):

  x1 = x[0]
  x2 = x[1]
  x3 = x[2]
  return np.array([
    3*x1 - math.cos(x2*x3) - 3/2,
    4*x1**2 - 625*x2**2 + 2*x2 -1,
    math.exp(-x1*x2) + 20*x3 + (10*math.pi - 3)/3
  ])

def J(x):
  x1 = x[0]
  x2 = x[1]
  x3 = x[2]
  return np.array([
    [3, math.sin(x2*x3)*x3,  math.sin(x2*x3)*x2],
    [8*x1, -1250*x2 + 2, 0],
    [-x2*math.exp(-x1*x2), -x1*math.exp(-x1*x2), 20]
  ])

def error(x):
  return 0.5 * ((x**2 - 1)**2)

def solve():
  x = np.array([5, 5, 5])

  for i in range(100):
    g = G(x)
    j = J(x)

    delta = np.linalg.solve(j, -g)
    x = x + delta
  
  g = G(x)
  print(x)
  print(np.dot(g, g))


if __name__ == '__main__':

  start_time = time.time()

  solve()
  print(f'{(time.time() - start_time) * 1000} ms')