import numpy as np
import matplotlib
import matplotlib.pyplot as plt

matplotlib.use('TkAgg')

m = 1.0
c = m * (2.0 * np.pi) ** 2
print(f"Natual frequency: {np.sqrt(c/m)/(2 * np.pi)} Hz")

step = 0.001
X = np.array([1, 0], dtype=np.float64)

A = np.array([[0, 1], [-c/m, 0]], dtype=np.float64)
AI = np.linalg.inv(np.identity(len(A), dtype=np.float64) - A * step)

times = np.arange(0, 100, step)
positions = np.zeros_like(times)

for i, t in enumerate(times):
    positions[i] = X[0]
    X = AI @ X


plt.plot(times, positions)
plt.title("Spring-Mass System")
plt.xlabel("Time")
plt.ylabel("Position")


plt.show()
