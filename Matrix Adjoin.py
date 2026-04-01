import numpy as np

def adjoint_matrix(A):
    # Pastikan A berbentuk array NumPy
    A = np.array(A, dtype=float)
    n = A.shape[0]
    
    # Cek apakah matriks persegi
    if A.shape[0] != A.shape[1]:
        raise ValueError("Matriks harus persegi untuk memiliki adjoint.")
    
    # Matriks kofaktor
    cofactors = np.zeros((n, n))
    
    for i in range(n):
        for j in range(n):
            # Minor: hapus baris i dan kolom j
            minor = np.delete(np.delete(A, i, axis=0), j, axis=1)
            cofactors[i, j] = ((-1) ** (i + j)) * np.linalg.det(minor)
    
    # Adjoint adalah transpose dari matriks kofaktor
    adj = cofactors.T
    return adj

A = [[0, 7, 0],
     [-1, -1, 0],
     [2, 4, 7]]

print("\nAdjoint dari A:")
print(adjoint_matrix(A))
