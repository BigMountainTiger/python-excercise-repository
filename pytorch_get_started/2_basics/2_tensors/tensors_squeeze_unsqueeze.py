import torch

def test_tensors():
  
  t = torch.tensor([1, 0, 2, 3, 4])
  print(f'{t.shape} - {t}')

  t0 = t.unsqueeze(dim = 0)
  print(f'{t0.shape} - {t0}')

  t1 = t.unsqueeze(dim = 1 )
  print(f'{t1.shape} - {t1}')

if __name__ == '__main__':
  test_tensors()