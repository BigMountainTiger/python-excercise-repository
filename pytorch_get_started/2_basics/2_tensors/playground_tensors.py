import torch

def test_tensors():
  tensor = torch.tensor([1, 0, 2, 3, 4])
  tensor.shape
  tensor.unsqueeze(dim=0).shape
  tensor.unsqueeze(dim=1).shape

if __name__ == '__main__':
  test_tensors()