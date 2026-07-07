import numpy as np

# Matriks A
A = np.array([
    [0.848, 0.152],
    [0.038, 0.962]
])

# Menghitung A^2
A87 = np.linalg.matrix_power(A, 87)

# Menghitung A^3
A88 = np.linalg.matrix_power(A, 87)

# Menghitung A^5
A5 = np.linalg.matrix_power(A, 5)

print("A =")
print(A)

print("\nA^87 =")
print(A87)

print("\nA^88 =")
print(A88)

print("\nA^5 =")
print(A5)