import torch
import numpy as np

def test_tensors():
  
  # Initializing a Tensor
  def initialize_a_tensor():
    data = [[1, 2],[3, 4]]

    # Directly from data
    x_data = torch.tensor(data)

    # From a NumPy array
    np_array = np.array(data)
    x_np = torch.from_numpy(np_array)

    # From another tensor
    x_ones = torch.ones_like(x_data)
    x_rand = torch.rand_like(x_data, dtype=torch.float)

    # With random or constant values:
    shape = (2,3)
    rand_tensor = torch.rand(shape)
    ones_tensor = torch.ones(shape)
    zeros_tensor = torch.zeros(shape)

    print('Done - initialize_a_tensor\n')

  initialize_a_tensor()

  # Attributes of a Tensor
  def attributes_of_a_tensor():
    tensor = torch.rand([3,4])

    print(f"Shape of tensor: {tensor.shape}")
    print(f"Datatype of tensor: {tensor.dtype}")
    print(f"Device of tensor is stored on: {tensor.device}")

    print('Done - attributes_of_a_tensor\n')

  attributes_of_a_tensor()

  # Operations on Tensors
  def operations_on_tensors():
    if torch.cuda.is_available():
      tensor = tensor.to('cuda')
    
    # 1. Standard numpy-like indexing and slicing:
    tensor = torch.rand(4, 4)
    print('First row: ',tensor[0])
    print('Last row:', tensor[-1, ...])
    print('First column: ', tensor[:, 0])
    print('Last column:', tensor[..., -1])
    tensor[:,1] = 0
    print(tensor)

    # 2. Joining tensors
    t1 = torch.cat([tensor, tensor, tensor], dim=1)
    print(t1)

    # 3. Arithmetic operations
    # This computes the matrix multiplication between two tensors. y1, y2, y3 will have the same value
    y1 = tensor @ tensor.T
    y2 = tensor.matmul(tensor.T)

    y3 = torch.rand_like(tensor)
    torch.matmul(tensor, tensor.T, out=y3)

    # This computes the element-wise product. z1, z2, z3 will have the same value
    z1 = tensor * tensor
    z2 = tensor.mul(tensor)

    z3 = torch.rand_like(tensor)
    torch.mul(tensor, tensor, out=z3)

    # 4. Single-element tensors
    agg = tensor.sum()
    agg_item = agg.item()
    print(agg_item, type(agg_item))

    # In-place operations
    print(tensor, "\n")
    tensor.add_(5)
    print(tensor)

    print('Done - operations_on_tensors\n')

  operations_on_tensors()

  # Bridge with NumPy
  def bridge_with_numpy():

    # Tensor to NumPy array
    # A change in the tensor reflects in the NumPy array
    t = torch.ones(5)
    print(f"t: {t}")
    n = t.numpy()
    print(f"n: {n}")

    t.add_(1)
    print(f"t: {t}")
    print(f"n: {n}")

    # NumPy array to Tensor
    # Changes in the NumPy array reflects in the tensor
    n = np.ones(5)
    t = torch.from_numpy(n)

    np.add(n, 1, out=n)
    print(f"t: {t}")
    print(f"n: {n}")

    print('Done - bridge_with_numpy')

  bridge_with_numpy()


if __name__ == '__main__':
  test_tensors()