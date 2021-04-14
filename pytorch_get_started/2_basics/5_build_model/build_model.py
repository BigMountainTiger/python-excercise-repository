import os
import torch
from torch import nn
from torch.utils.data import DataLoader
from torchvision import datasets, transforms

def build_model():
  device = 'cuda' if torch.cuda.is_available() else 'cpu'
  print('Using {} device'.format(device))

  # https://stackoverflow.com/questions/48619928/unable-to-learn-xor-representation-using-2-layers-of-multi-layered-perceptron-m
  # https://gist.github.com/RichardKelley/17ef5f2291c273de11540c33dc1bfbf2
  class NeuralNetwork(nn.Module):
    def __init__(self):
      super(NeuralNetwork, self).__init__()
      self.linear_relu_stack = nn.Sequential(
        nn.Linear(2, 3),
        nn.ReLU(),
        nn.Linear(3, 1),
        nn.ReLU()
      )

    def forward(self, x):
      logits = self.linear_relu_stack(x)
      return logits

  model = NeuralNetwork().to(device)
  print(model)

  X = torch.rand(1, 2, device=device)
  logits = model(X)

  print(logits)

if __name__ == '__main__':
  build_model()