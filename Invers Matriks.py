import numpy as np

# matriks A
A = np.array([
                [1, 0, 1],
                [-1, 1, 1],
                [0, 1, 0]
            ])

# Mengecek apakah matriks dapat diinvers (determinan ≠ 0)
det = np.linalg.det(A)
if det == 0:
    print("Matriks tidak memiliki invers (determinan = 0).")
else:
    A_inv = np.linalg.inv(A)
    print("Matriks A:")
    print(A)
    print("\nInvers dari A:")
    print(A_inv)