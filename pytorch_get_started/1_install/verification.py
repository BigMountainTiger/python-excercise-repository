import torch

def verify():
  x = torch.rand(5, 3)
  print(type(x))
  print(x)

if __name__ == '__main__':
  verify()