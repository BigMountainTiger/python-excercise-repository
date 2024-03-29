import torch
from torch import nn
from torch import optim
from torch.autograd import Variable
import numpy as np

class NeuralNetwork(nn.Module):

  def __init__(self):
    super(NeuralNetwork, self).__init__()
    self.linear_relu_stack = nn.Sequential(
      nn.Linear(2, 5),
      nn.ReLU(),
      nn.Linear(5, 1)
    )

  def forward(self, x):
    logits = self.linear_relu_stack(x)
    return logits

def build_model_excercise():
  model = NeuralNetwork()
  
  loss_fn = nn.MSELoss()
  optimizer = optim.Adam(model.parameters(), lr=1e-3)

  state = np.array([[0., 0.], [0., 1.], [1., 0.], [1., 1.]])
  label = np.array([[0.], [1.], [1.], [0.]])

  epoch = 3000
  for i in range(epoch):
    
    for batch in range(4):
      state_var = torch.Tensor(state)
      label_var = torch.Tensor(label)

      # state_var = Variable(torch.Tensor(state))
      # label_var = Variable(torch.Tensor(label))

      pred = model(state_var)
      loss = loss_fn(pred, label_var)

      optimizer.zero_grad()
      loss.backward()
      optimizer.step()

  print('Function after training:')
  with torch.no_grad():
    print(f'f(0,0) = {model(torch.Tensor([0.0, 0.0]))}')
    print(f'f(0,1) = {model(torch.Tensor([0.0, 1.0]))}')
    print(f'f(1,0) = {model(torch.Tensor([1.0, 0.0]))}')
    print(f'f(1,1) = {model(torch.Tensor([1.0, 1.0]))}')

    # Access tensor element by numpy
    v = model(torch.Tensor([1.0, 0.0]))
    print(v.numpy()[0])

  print("f(1,1) = {}".format(model(Variable(torch.Tensor([1.0,1.0]).unsqueeze(0)))))

  # https://pytorch.org/tutorials/beginner/saving_loading_models.html
  print('Save the model')
  modeldir = '../../nn_model'
  path = f'{modeldir}/excercise.model'
  torch.save(model, path)

  print('Load the model')
  loaded_model = torch.load(path)

  print('Use the model')
  with torch.no_grad():
    print("f(1,1) = {}".format(loaded_model(torch.Tensor([1.0,1.0]))))

# This is re-written so get more excercise
# How are optimizer.step() and loss.backward() related?
# https://discuss.pytorch.org/t/how-are-optimizer-step-and-loss-backward-related/7350
if __name__ == '__main__':
  build_model_excercise()