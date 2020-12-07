
def integrate():
  e = 2.718281828459045
  steps = 10000
  step_length = 1.0 / steps

  def prime(x):
    return pow(e, -(x * x))

  def delta(x):
    return step_length * (prime(x) + prime(x - step_length)) / 2

  x = 0
  i = 0
  for step in range(steps):
    x += step_length
    i += delta(x)

  print()
  print(f'The result is {i}')

if __name__ == '__main__':
  integrate()
