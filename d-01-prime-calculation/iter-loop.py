def calculate():
  a = -2
  b = 1

  i = 1
  while i <= 30:
    my_srt = (a*a + b*b)**(1/2)
    at = a + b + my_srt
    bt = a + b - my_srt

    a = at
    b = bt

    print('{} => a = {}, b = {}'.format(i, a, b))
    i += 1

if __name__ == '__main__':
  calculate()