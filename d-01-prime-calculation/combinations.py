import itertools

M = (66, -37.5, 142857, -1, -2, 0, 3.1415926535)

def prod(val) :  
  result = 1
  for e in val:  
      result *= e

  return result

def combinations():

  COMBINATIONS = []

  for i in range(1, 8):
    COMBINATIONS.extend(itertools.combinations(M, i))

  result = 0
  for c in COMBINATIONS:
    result += prod(c)

  print(f'Total {len(COMBINATIONS)} combinations the sum = {result}')
  print('结果是负1？')

if __name__ == '__main__':
  combinations()
