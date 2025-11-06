import numpy as np
A = np.array([[1, 2, 3],
              [0, 1, 4],
              [5, 6, 0]])

try:
    np.linalg.inv(A)
    print(np.linalg.inv(A))
except:
    print("Matriks tidak punya invers karena determinannya nol atau matriks singular.")