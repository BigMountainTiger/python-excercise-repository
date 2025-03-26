i = 0

def print_i():
  print(f'The value of i = {i}')

def increase_i():
  global i
  print(f'Increment i = {i} by 1')
  i += 1