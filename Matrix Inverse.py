import numpy as np
A = np.array([[6, 1, 0],
              [-1, 1, 1],
              [0, 1, 0]])

try:
    np.linalg.inv(A)
    print(np.linalg.inv(A))
except:
    print("Matriks tidak punya invers karena determinannya nol atau matriks singular.")