import torch
import numpy as np

def tensors_access_elements():
  t = torch.Tensor([1234])
  print(t)
  print(t.size())
  print(t.item())


if __name__ == '__main__':
  tensors_access_elements()