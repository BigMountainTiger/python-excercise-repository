import torch

def test_tensors():
  
  def test_1():
    t = torch.tensor([1, 0, 2, 3, 4])
    print(f'{t.shape} - {t}')

    t0 = t.unsqueeze(dim = 0)
    print(f'{t0.shape} - {t0}')

    t1 = t.unsqueeze(dim = 1 )
    print(f'{t1.shape} - {t1}')

    s0 = t0.squeeze()
    print(f'{s0.shape} - {s0}')

    s1 = t1.squeeze()
    print(f'{s1.shape} - {s1}')

  # test_1()

  def test_2():
    t = torch.randn(3, 32, 32)
    print(t.shape)

    t0 = t.unsqueeze(dim = 0)
    print(t0.shape)

    t1 = t.unsqueeze(dim = 1)
    print(t1.shape)

    t2 = t.unsqueeze(dim = 2)
    print(t2.shape)

    t3 = t.unsqueeze(dim = 3)
    print(t3.shape)

  # test_2()

  def test_3():

    t = torch.tensor(100)
    print(t.shape)

    t0 = t.unsqueeze(dim=0)
    print(t0.shape)

    t1 = t0.unsqueeze(dim=0)
    print(t1.shape)

    s = t1.squeeze()
    print(s.shape)


  test_3()

if __name__ == '__main__':
  test_tensors()