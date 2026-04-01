import numpy as np
A = np.array([[2, 4, -4],
              [-4, 3, -3],
              [2, -2, 2]])

try:
    np.linalg.inv(A)
    print(np.linalg.inv(A))
except:
    print("Matriks tidak punya invers karena determinannya nol atau matriks singular.")