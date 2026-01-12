from torchvision import datasets
from torchvision.transforms import ToTensor, Lambda

def transforms():
  datadir = '../../nn_data'
  ds = datasets.FashionMNIST(
    root=datadir,
    train=True,
    download=True,
    transform=ToTensor(),
    target_transform=Lambda(lambda y: torch.zeros(10, dtype=torch.float).scatter_(0, torch.tensor(y), value=1))
  )

if __name__ == '__main__':
  transforms()