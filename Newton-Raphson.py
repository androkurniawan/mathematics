import math

def f(x):
    return math.exp(x) - 4*x - 1

def f_prime(x):
    return math.exp(x) - 4

x0 = 3
tol = 0.0001  
max_iter = 5

for i in range(max_iter):
    fx = f(x0)
    fpx = f_prime(x0)

    if fpx == 0:
        print("Turunan nol! Metode gagal.")
        break

    x1 = x0 - fx/fpx

    print(f"Iterasi {i+1}")
    print(f"   x = {x0:.6f}")
    print(f"   f(x) = {fx:.6f}")
    print(f"   f'(x) = {fpx:.6f}")
    print(f"   x_1 = {x1:.6f}")
    print()

    # syarat berhenti berdasarkan toleransi
    if abs(x1 - x0) < tol:
        print(f"Konvergen pada x ≈ {x1}")
        break

    x0 = x1
else:
    print("Tidak konvergen dalam jumlah iterasi maksimum.")
