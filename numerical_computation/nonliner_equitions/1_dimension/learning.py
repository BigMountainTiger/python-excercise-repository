# solve x^2 = 1
# Min 1/2*(x^2 - 1)^2

import time

def prime(x):
  return (x**2 - 1) * 2 * x

def error(x):
  return 0.5 * ((x**2 - 1)**2)

def solve():

  x = 5
  learning_rate = 0.01

  for i in range(60000):
    x = x - learning_rate * prime(x)

  print(f'x={x} error={error(x)}')



if __name__ == '__main__':

  start_time = time.time()
  solve()

  print(f'{(time.time() - start_time) * 1000} ms')