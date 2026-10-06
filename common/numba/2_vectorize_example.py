import numpy as np
from numba import vectorize

# nopython default to True
# target default to cpu (single-core)
@vectorize(['float64(float64, float64)'], nopython=True, target='parallel')
def scalar_add_and_multiply(x, y):
    return (x + y) * 2

arr1 = np.array([1.0, 2.0, 3.0], dtype=np.float64)
arr2 = np.array([4.0, 5.0, 6.0], dtype=np.float64)

result = scalar_add_and_multiply(arr1, arr2)
print(result)
