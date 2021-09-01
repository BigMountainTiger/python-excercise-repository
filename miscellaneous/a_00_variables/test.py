import module_1

# Python variable is passed by value
def passing_by_value():
  print('passing_by_value()')
  def add(i):
    i += 1
    print(f'Increment in function - i = {i}')

  i = 0
  add(i)

  print(f'The variable remains the same in the calling function - i = {i}')
  print(f'Variables are passed by value')
  print()

# Python modules are objects
def module_is_object():
  print('module_is_object()')

  module_1.i = 100
  module_1.print_i()
  module_1.increase_i()
  module_1.print_i()
  print('A module is an object')
  print()

if __name__ == '__main__':
  passing_by_value()
  module_is_object()