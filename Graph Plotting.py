import numpy as np
import matplotlib.pyplot as plt

# Definisi fungsi
def f(x):
    # return np.exp(2*x) - 3
    # return x**3 + 200
    return np.exp(-x) - x

# Buat data x dari -2 sampai 2 (100 titik)
x = np.linspace(-2, 2, 100)
y = f(x)

# Plot grafik
plt.plot(x, y, label="f(x) = e^(-x) - x", color="blue")

# Tambahkan sumbu X dan Y
plt.axhline(0, color="black", linewidth=0.8)
plt.axvline(0, color="black", linewidth=0.8)

# Tambahkan judul dan label
# plt.title("Grafik f(x) = e^(2x) - 3")
plt.xlabel("x")
plt.ylabel("f(x)")
plt.legend()
plt.grid(True)

# Tampilkan
plt.show()
