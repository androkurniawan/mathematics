import numpy as np

A = np.array([[8, 0],
              [-1, 2],
              [1, 1]])

B = np.array([[8, 0],
              [0, 2]])

C = np.dot(A, B)
print(C)
