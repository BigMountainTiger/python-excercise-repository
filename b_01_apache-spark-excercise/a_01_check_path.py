import sys, inspect, pyspark

print('Python package path:')
for path in sys.path:
  print(path)

print('Inspect sys - {}'.format(inspect.getmodule(sys)))
print('Inspect pyspark - {}'.format(inspect.getmodule(pyspark)))