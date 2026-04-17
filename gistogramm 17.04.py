import matplotlib.pyplot as plt
import numpy as np

x_axis = np.linspace(-5, 5, 100)
values = np.sin(x_axis)

weights = (values + 1) * 50 # для повторения ( 1 положительными для весов)
plt.figure(figsize=(10, 5))
plt.hist(x_axis, bins=100, weights=weights, edgecolor='black', alpha=0.7)

plt.grid(True)
plt.show()