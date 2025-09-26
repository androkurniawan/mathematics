import numpy as np
import matplotlib.pyplot as plt
import mplcursors

# Definisi fungsi
def f(x):
    # return x**3 + 200
    # return np.exp(2*x) - 3
    # return np.exp(-x) - 2*x
    return 23*x**7 - 125*x**6 + 120*x**4 - 15*x**3 + 120*x**2 - 3


# Buat data x dari -10 sampai 10 (100 titik)
x = np.linspace(-1, 1, 100)
y = f(x)

# Plot grafik
fig, ax = plt.subplots()
line, = ax.plot(x, y, label="f(x) = x^3 + 200", color="blue")

# Tambahkan sumbu X dan Y
ax.axhline(0, color="black", linewidth=0.8)
ax.axvline(0, color="black", linewidth=0.8)

# Tambahkan judul dan label
ax.set_title("Grafik f(x) = x^3 + 200")
ax.set_xlabel("x")
ax.set_ylabel("f(x)")
ax.legend()
ax.grid(True)

# Aktifkan hover tooltip
mplcursors.cursor(line, hover=True)

plt.show()
