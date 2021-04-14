import torch
from torch import nn
from torch.utils.data import DataLoader
from torchvision import datasets
from torchvision.transforms import ToTensor, Lambda, Compose
import matplotlib.pyplot as plt

def quickstart():
  data_directory = 'nn_data'
  training_data = datasets.FashionMNIST(root=data_directory, train=True, download=True, transform=ToTensor())
  test_data = datasets.FashionMNIST(root=data_directory, train=False, download=True, transform=ToTensor())

if __name__ == '__main__':
  quickstart()