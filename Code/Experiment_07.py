import numpy as np

# Stored pattern
pattern = np.array([1, 1, -1, -1])

# Weight matrix
W = np.outer(pattern, pattern)
np.fill_diagonal(W, 0)

# Noisy input
x = np.array([1, 1, 1, -1])

# Recall
x = np.where(W @ x >= 0, 1, -1)

print("Original Pattern:", pattern)
print("Noisy Pattern:", [1, 1, 1, -1])
print("Recalled Pattern:", x)
