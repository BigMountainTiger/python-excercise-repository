import os
import torch
from torch import nn
from torch import optim
from torch.autograd import Variable
from torch.utils.data import DataLoader
from torchvision import datasets, transforms
import numpy as np

def build_model():
  device = 'cuda' if torch.cuda.is_available() else 'cpu'
  print('Using {} device'.format(device))

  # https://stackoverflow.com/questions/48619928/unable-to-learn-xor-representation-using-2-layers-of-multi-layered-perceptron-m
  # https://gist.github.com/RichardKelley/17ef5f2291c273de11540c33dc1bfbf2
  class NeuralNetwork(nn.Module):
    def __init__(self):
      super(NeuralNetwork, self).__init__()
      self.linear_relu_stack = nn.Sequential(
        nn.Linear(2, 10),
        nn.ReLU(),
        nn.Linear(10, 1),
      )

    def forward(self, x):
      logits = self.linear_relu_stack(x)
      return logits

  model = NeuralNetwork().to(device)
  print(model)

  X = torch.rand(1, 2, device=device)
  logits = model(X)
  print(logits)

  loss_fn = nn.MSELoss()
  optimizer = optim.Adam(model.parameters(), lr=1e-3)

  training_epochs = 3000

  pairs = [(np.asarray([0.0,0.0]), [0.0]),
    (np.asarray([0.0,1.0]), [1.0]),
    (np.asarray([1.0,0.0]), [1.0]),
    (np.asarray([1.0,1.0]), [0.0])
  ]

  state_matrix = np.vstack([x[0] for x in pairs])
  label_matrix = np.vstack([x[1] for x in pairs])

  for i in range(training_epochs):
        
    for batch_ind in range(4):
      minibatch_state_var = Variable(torch.Tensor(state_matrix))
      minibatch_label_var = Variable(torch.Tensor(label_matrix))
              
      y_pred = model(minibatch_state_var)
      
      loss = loss_fn(y_pred, minibatch_label_var)
      # print(i, batch_ind, loss.data[0])

      optimizer.zero_grad()
      loss.backward()
      optimizer.step()

  print('Function after training:')
  print("f(0,0) = {}".format(model(Variable(torch.Tensor([0.0,0.0]).unsqueeze(0)))))
  print("f(0,1) = {}".format(model(Variable(torch.Tensor([0.0,1.0]).unsqueeze(0)))))
  print("f(1,0) = {}".format(model(Variable(torch.Tensor([1.0,0.0]).unsqueeze(0)))))
  print("f(1,1) = {}".format(model(Variable(torch.Tensor([1.0,1.0]).unsqueeze(0)))))

if __name__ == '__main__':
  build_model()