A = pow(2016, 239) - 1
result = []

def calculate():
  data = None
  with open('primes.txt', 'r') as file:
    data = file.read().split('\n');

  for d in data:
    if len(result) == 6:
      break

    for n in d.split('\t'):
      p = int(n)
      if A % p == 0:
        result.append(p)

  print(result)

if __name__ == '__main__':
  calculate()