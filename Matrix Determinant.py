import numpy as np

A = np.array([[1, 0, 1],
              [-1, 1, 1],
              [0, 1, 0]])
sign, logdet = np.linalg.slogdet(A)
res = sign * np.exp(logdet)

print(res)