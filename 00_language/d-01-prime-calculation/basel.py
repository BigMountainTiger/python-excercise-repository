def calculate():
  X = 0

  t = 100 * 10000
  for i in range(1, t + 1):
    X = X + (1 / pow(i, 2))

  print(X)

if __name__ == '__main__':
  calculate()