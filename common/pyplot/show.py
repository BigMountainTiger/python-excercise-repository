# sudo apt install python3.11-tk
# Need to install the version specific tk package, e.g., python3.11-tk for Python 3.11

# pip install matplotlib

import matplotlib
import matplotlib.pyplot as plt

matplotlib.use('TkAgg')

x = [1, 2, 3, 4, 5]
y = [2, 4, 6, 8, 10]

plt.plot(x, y, marker='o', color='blue')
plt.title("My Standalone Plot")
plt.xlabel("X Axis")
plt.ylabel("Y Axis")


plt.show()
