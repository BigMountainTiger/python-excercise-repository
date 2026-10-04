import time
from functools import wraps
import numpy as np
from numba import njit


def timeit(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        start = time.time()
        func_result = func(*args, **kwargs)
        print(f"Execution time: {(time.time() - start):.5f} seconds")

        return func_result

    return wrapper

# Experiment shows arr.sum() has the best speed even without numba
# ----------------------------------------------------------------


def sum_array_python_with_numpy_sum(arr):
    total = arr.sum()
    return total


def sum_array_python(arr):
    total = 0.0
    for i in range(arr.shape[0]):
        total += arr[i]
    return total


timed_sum_array_python = timeit(sum_array_python)
timed_sum_array_python_with_numpy_sum = timeit(sum_array_python_with_numpy_sum)

# 1. njit is unable to handle the timeit decorator, so we apply it after njit
# 2. by default nogil is False. But releasing the GIL did not help the speed in this case
timed_sum_array_numba = timeit(njit(nogil=True)(sum_array_python))


large_array = np.random.random(10_000_000)

print("Running sum_array_python_with_numpy_sum")
print("numpy_sum has the best speed")
result = timed_sum_array_python_with_numpy_sum(large_array)
print(f"Result: {result}")

print()
print("Running pure Python")
result = timed_sum_array_python(large_array)
print(f"Result: {result}")

print()
print("Running Numba version")
result = timed_sum_array_numba(large_array)
print(f"Result: {result}")

print()
print("Running Numba version again")
result = timed_sum_array_numba(large_array)
print(f"Result: {result}")
