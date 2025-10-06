v = 'This is v'

def function_scope():
  v = 'This is function v. It starts a new scope'
  print(v)

def a_variable_can_not_be_both_local_and_glocal():
  v = 'A local declaration'
  print(v)

  # It is a syntax error
  # global v

def use_global_variable():
  global v
  v = 'Declared as global'
  print(v)

def conclusion():
  print('1. Python variables delcared in function has function scope')
  print('2. To use global variable, need to use global keyord')
  print('3. It is a syntax error if a local variable already declared before global keyword is used')

def run():
  print(v)
  function_scope()
  print(v)
  print()

  a_variable_can_not_be_both_local_and_glocal()
  print()

  print(v)
  use_global_variable()
  print(v)
  print()
  
  conclusion()


if __name__ == '__main__':
  run()