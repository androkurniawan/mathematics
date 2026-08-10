import numpy as np
A = np.array([[1, 2, 3],
              [2, 5, 3],
              [1, 0, 8]])

try:
    np.linalg.inv(A)
    print(np.linalg.inv(A))
except:
    print("Matriks tidak punya invers karena determinannya nol atau matriks singular.")