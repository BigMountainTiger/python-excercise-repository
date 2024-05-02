note = []

note.append('# Look at the package_1/dir_1/module_1.py file')
note.append('# "." means current directory, ".." parent directory, "..." one more parent above.')
note.append('# Relative import above top-level package is an error')

def printIt():
  print('Print from module_2:\n')

  for n in note:
    print(n)

  print('OK')
