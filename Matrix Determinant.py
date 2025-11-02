import numpy as np

A = np.array([[-1, 1, 2],
              [3, 0, -5],
              [1, 7, 2]])
sign, logdet = np.linalg.slogdet(A)
res = sign * np.exp(logdet)

print(res)