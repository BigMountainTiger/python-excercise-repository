from primes import primes

A = pow(2016, 239) - 1

def calculate():
  for i in primes: 
    print(i)

  # print(A)

if __name__ == '__main__':
  calculate()