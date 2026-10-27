import numpy as np
import matplotlib.pyplot as plt
x = np.arange(0, 11)
# Triangular
tri = np.maximum(np.minimum((x-2)/3, (8-x)/3), 0)
# Trapezoidal
trap = np.maximum(np.minimum(np.minimum((x-2)/2, 1), (8-x)/2), 0)
# Gaussian
gauss = np.exp(-((x-5)**2)/(2*1.5**2))
# Plot
plt.plot(x, tri, label="Triangular")
plt.plot(x, trap, label="Trapezoidal")
plt.plot(x, gauss, label="Gaussian")
plt.xlabel("Input")
plt.ylabel("Membership")
plt.legend()
plt.grid()
plt.show()
