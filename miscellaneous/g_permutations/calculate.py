import itertools

def labelIt(i):
  return {
    'A': i[0],
    'B': i[1],
    'C': i[2],
    'D': i[3],
    'E': i[4],
    'F': i[5],
    'G': i[6],
    'H': i[7],
    'I': i[8],
  }

def validate(e):
  l = e['A'] + e['B'] + e['C']

  if (l != (e['A'] + e['E'])):
    return False

  if (l != (e['B'] + e['F'] + e['I'])):
    return False

  if (l != (e['A'] + e['G'] + e['H'])):
    return False

  if (l != (e['D'] + e['E'] + e['F'])):
    return False

  if (l != (e['D'] + e['G'] + e['I'])):
    return False

  if (l != (e['H'] + e['I'])):
    return False

  return True

  

def calculate():
  candidates = [1, 2, 3, 4, 5, 6, 7, 8, 9]
  permutations = itertools.permutations(candidates)

  solutions = []
  for item in permutations:
    e = labelIt(item)
    if validate(e):
      solutions.append(e)

  for i in range(len(solutions)):
    item = solutions[i]
    print(f'Solution No.{i + 1}:')
    for a, v in item.items():
      print(f'{a} - {v}')

if __name__ == '__main__':
  calculate()