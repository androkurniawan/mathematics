import tkinter as tk
from tkinter import messagebox

def tambah_item():
    try:
        produk = entry_produk.get()
        harga = float(entry_harga.get())
        jumlah = int(entry_jumlah.get())

        subtotal = harga * jumlah

        item = {
            "produk": produk,
            "harga": harga,
            "jumlah": jumlah,
            "subtotal": subtotal
        }

        daftar_belanja.append(item)

        text_daftar.config(state="normal")
        text_daftar.insert(
            tk.END,
            f"{produk} - {jumlah} x Rp{harga:.2f} = Rp{subtotal:.2f}\n"
        )
        text_daftar.config(state="disabled")

        entry_produk.delete(0, tk.END)
        entry_harga.delete(0, tk.END)
        entry_jumlah.delete(0, tk.END)

    except ValueError:
        messagebox.showerror(
            "Error",
            "Masukkan harga dan jumlah yang valid!"
        )

def hitung_total():
    total = sum(item["subtotal"] for item in daftar_belanja)
    label_total.config(text=f"{total:.2f}")

def bersihkan():
    daftar_belanja.clear()

    text_daftar.config(state="normal")
    text_daftar.delete("1.0", tk.END)
    text_daftar.config(state="disabled")

    label_total.config(text="0")

# ---------------------------
# Window utama
# ---------------------------

root = tk.Tk()
root.title("Program Kasir Sederhana")
root.geometry("500x400")

daftar_belanja = []

# Input Produk
tk.Label(root, text="Nama Produk:").grid(row=0, column=0, padx=5, pady=5, sticky="w")
entry_produk = tk.Entry(root, width=30)
entry_produk.grid(row=0, column=1, padx=5, pady=5)

# Input Harga
tk.Label(root, text="Harga:").grid(row=1, column=0, padx=5, pady=5, sticky="w")
entry_harga = tk.Entry(root, width=30)
entry_harga.grid(row=1, column=1, padx=5, pady=5)

# Input Jumlah
tk.Label(root, text="Jumlah:").grid(row=2, column=0, padx=5, pady=5, sticky="w")
entry_jumlah = tk.Entry(root, width=30)
entry_jumlah.grid(row=2, column=1, padx=5, pady=5)

# Tombol
tk.Button(root, text="Tambah", command=tambah_item).grid(row=3, column=0, pady=10)
tk.Button(root, text="Hitung Total", command=hitung_total).grid(row=3, column=1, pady=10)
tk.Button(root, text="Bersihkan", command=bersihkan).grid(row=3, column=2, pady=10)

# Daftar Belanja
tk.Label(root, text="Daftar Belanja:").grid(row=4, column=0, padx=5, pady=5, sticky="w")

text_daftar = tk.Text(root, width=55, height=10, state="disabled")
text_daftar.grid(row=5, column=0, columnspan=3, padx=5, pady=5)

# Total
tk.Label(root, text="Total: Rp").grid(row=6, column=0, padx=5, pady=10, sticky="e")
label_total = tk.Label(root, text="0")
label_total.grid(row=6, column=1, sticky="w")

root.mainloop()