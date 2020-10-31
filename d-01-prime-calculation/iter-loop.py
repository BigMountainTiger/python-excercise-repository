import math

def calculate():
  a = -2
  b = 1

  i = 1
  while i <= 2020:
    sqrt = math.sqrt(a*a + b*b)
    if math.isnan(sqrt):
      break

    at = a + b + sqrt
    bt = a + b - sqrt

    a = at
    b = bt
    i += 1

  print('a_{} = {} - {}'.format(i - 1, a, b))

if __name__ == '__main__':
  calculate()