import numpy as np

A = np.array([[3, -1, 3],
              [1, 3, -4],
              [0, 1, -5]])
sign, logdet = np.linalg.slogdet(A)
res = sign * np.exp(logdet)

print(res)