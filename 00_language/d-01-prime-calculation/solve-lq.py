import numpy as np

def calculate():
  A = [[2, -1, 0, 0],
      [-1, 2, -1, 0],
      [0, -1, 2, -1],
      [0, 0, -1, 2]]
  b = [10, 0, 0, 25]

  X = np.linalg.solve(A, b)
  print(X)

if __name__ == '__main__':
  calculate()