import os
import torch
from torch import nn
from torch.utils.data import DataLoader
from torchvision import datasets, transforms

def build_model():
  device = 'cuda' if torch.cuda.is_available() else 'cpu'
  print('Using {} device'.format(device))

  class NeuralNetwork(nn.Module):
    def __init__(self):
      super(NeuralNetwork, self).__init__()
      self.linear_relu_stack = nn.Sequential(
        nn.Linear(2, 3),
        nn.ReLU(),
        nn.Linear(3, 3),
        nn.ReLU(),
        nn.Linear(3, 2),
        nn.ReLU()
      )

    def forward(self, x):
      logits = self.linear_relu_stack(x)
      return logits

  model = NeuralNetwork().to(device)
  print(model)

if __name__ == '__main__':
  build_model()