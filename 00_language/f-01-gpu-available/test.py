import GPUtil

def check_if_gpu():
  gpus = GPUtil.getAvailable()

  if (len(gpus) == 0):
    print('No gpu found')
  else:
    print(gpus)

if __name__ == '__main__':
  check_if_gpu()