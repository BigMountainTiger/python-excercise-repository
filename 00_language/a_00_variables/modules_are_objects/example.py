import module_1

# Python modules are objects
def module_is_object():
  print('module_is_object()')

  print('Set the value of i out of the module')
  module_1.i = 100
  module_1.print_i()

  print()
  print('Increment the value of i from out of the module')
  module_1.increase_i()
  module_1.print_i()

  print()
  print('Conclusion')
  print('A module is an object')
  print()

if __name__ == '__main__':
  module_is_object()