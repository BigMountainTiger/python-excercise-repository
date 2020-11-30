# Prime numbers smaller than 1000
from primes import primes

A = pow(2016, 239) - 1
result = []

def calculate():
  for p in primes: 
    if A % p == 0:
      result.append(p)

    if len(result) == 6:
      break

  print(result)

if __name__ == '__main__':
  calculate()