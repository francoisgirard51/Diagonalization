# Matrix calculus: Beginner level 1

import numpy as np

A = np.array([[1, 2, 3],
              [4, 5, 6]])

X = np.array([[7],
              [8],
              [9]])

Y = np.dot(A,X)
print("Matrix product 𝑌 = 𝐴𝑋:\n", Y)
print("\nMatrix A:\n", A)
print("\nVector Y:\n", Y)
print("\nVector X:\n", X)
