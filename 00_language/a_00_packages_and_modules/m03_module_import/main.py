# from module_1 import add_number
# from module_1 import print_number
# from module_1 import number

number = 0

def number_in_function():

  def add_number_func(number):
    number = 2
    print(f'Number in function - {number}')

  add_number_func(number)
  print(f'Number out of the function - {number}')

  def add_directly():
    global number
    number = 3
    print(number)

  add_directly()
  print(f'Number out of the function - {number}')

def variable_in_module():
  
  add_number()
  print_number()

  global number
  print(f'Imported number = {number}')

  number = 6
  print_number()

if __name__ == '__main__':
  # variable_in_module()
  number_in_function()