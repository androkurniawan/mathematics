# Metode Regula Falsi (langsung eksekusi)
import math

def f(x):
    # return x**2 - 10*x + 23
    return math.log(x) - 5 + x

# Interval awal
a = 3
b = 4

tol = 1e-60
max_iter = 5

fa = f(a)
fb = f(b)

if fa * fb > 0:
    print("f(a) dan f(b) harus berbeda tanda.")
else:
    for i in range(max_iter):
        # Rumus Regula Falsi
        c = (a*fb - b*fa) / (fb - fa)
        fc = f(c)

        print(f"Iterasi {i+1}: a={a:.6f}, b={b:.6f}, c={c:.6f}, f(c)={fc:.6f}")

        # Cek toleransi
        if abs(fc) < tol:
            break

        # Update interval
        if fa * fc < 0:
            b = c
            fb = fc
        else:
            a = c
            fa = fc

    print("\nAkar hampiran =", c)
