v = 'This is the global variable'

def print_local():
  v = 'This is the local variable'
  print(f'{hex(id(v))} - {v}')

def print_global():
  global v
  print(f'{hex(id(v))} - {v}')

def pass_variable(p):
  p = 'Modified in function'
  print(f'{hex(id(p))} - {p}')


def run():
  # print_local()
  # print_global()

  global v
  print(f'{hex(id(v))} - {v}')
  pass_variable(v)
  v = 'ABCD'
  
  print_global()


if __name__ == '__main__':
  run()