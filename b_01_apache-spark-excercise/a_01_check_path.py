import sys, inspect

print('Python package path:')
for path in sys.path:
  print(path)

print('Inspect sys - {}'.format(inspect.getmodule(sys)))