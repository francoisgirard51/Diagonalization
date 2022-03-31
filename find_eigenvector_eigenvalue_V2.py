#

import numpy as np

A = np.array([[1, 2],
              [3, 4]])
I = np.identity(2)

B = (np.dot(c1, I) - A)

V2 = np.array([[10],
              [5]])

print('Matrix B =',B)

for n in range (10):
    c2 = np.linalg.norm(V2)
    W2 = ((1/c2)*V2)
    V2 = np.dot(B, W2)

    print('\n- ', c2, W2)
