import numpy as np
import matplotlib
import matplotlib.pyplot as plt

matplotlib.use('TkAgg')

m = 1.0
c = m * (2.0 * np.pi) ** 2
A = np.array([[0, 1], [-c/m, 0]], dtype=np.float64)
print(f"Natual frequency: {np.sqrt(c/m)/(2 * np.pi)} Hz")

h = 0.01
X = np.array([1, 0], dtype=np.float64)

times = np.arange(0, 10, h)
positions = np.zeros_like(times)


def rk4_step(A, X, h):
    # It seems faster without numba njit :D
    k_1 = h * A @ X
    k_2 = h * A @ (X + 0.5 * k_1)
    k_3 = h * A @ (X + 0.5 * k_2)
    k_4 = h * A @ (X + k_3)
    return X + (k_1 + 2*k_2 + 2*k_3 + k_4) / 6


for i, t in enumerate(times):
    positions[i] = X[0]
    X = rk4_step(A, X, h)


plt.plot(times, positions)
plt.title("Spring-Mass System")
plt.xlabel("Time")
plt.ylabel("Position")


plt.show()
