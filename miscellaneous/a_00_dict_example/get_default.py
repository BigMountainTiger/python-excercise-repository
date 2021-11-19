def run():
  d = {}

  print('1. Key not found - "get()" return the default value but the dictionary is not  modified')
  a = d.get('A', 0)
  print(a)
  print(d)


  print('Key not found - "setdefault()" set the default value and return it')
  a = d.setdefault('A', 0)
  print(a)
  print(d)

  print('Key is found - "setdefault()" get the value')
  d['A'] = 1
  a = d.setdefault('A', 0)
  print(a)
  print(d)

if __name__ == '__main__':
  run()