import numpy as np
import matplotlib
import matplotlib.pyplot as plt

matplotlib.use('TkAgg')

c, m, step = 10.0, 1.0, 0.01
X = np.array([0, 1], dtype=np.float64)

A = np.array([[0, 1], [-c/m, 0]], dtype=np.float64)
AL = np.identity(len(A), dtype=np.float64) + A * step

times = np.arange(0, 100, step)
positions = np.zeros_like(times)

for i, t in enumerate(times):
    positions[i] = X[0]
    X = AL @ X

plt.plot(times, positions)
plt.title("Spring-Mass System")
plt.xlabel("Time")
plt.ylabel("Position")


plt.show()
