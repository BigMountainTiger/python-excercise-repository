# https://www.superprof.co.uk/resources/academic/maths/linear-algebra/linear-programming/linear-programming-examples.html
# f(x,y)= 50x + 40y
# 2x + 3y <= 1500
# 2x + y <= 1000
# x >= 0
# y >= 0

import numpy as np
import scipy.optimize as opt

def example_1():

  cost = np.array([-50, -40])

  A = [np.array([2, 3]), np.array([2, 1])]
  B = [1500, 1000]
  C = [(0, None), (0, None)]

  obj_fun = lambda x: np.sum(x*cost)
  cond = (
    {'type': 'ineq', 'fun': lambda x: B[0] - np.sum(A[0]*x)},
    {'type': 'ineq', 'fun': lambda x: B[1] - np.sum(A[1]*x)}
  )

  guess = [1, 1]

  result = opt.minimize(obj_fun, guess, method = 'SLSQP', bounds = C, constraints = cond)

  print(result)
  print(f'Result is {(result.x)[0]} - {(result.x)[1]}')

  print('Completed')

if __name__ == '__main__':
  example_1()