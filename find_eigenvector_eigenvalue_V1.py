#

import numpy as np

A = np.array([[1, 2],
              [3, 4]])
V1 = np.array([[5],
              [6]])

for n in range (10):
    c1 = np.linalg.norm(V1)
    W1 = ((1/c1)*V1)
    V1 = np.dot(A, W1)

    print('\n- ', c1, W1)
