import tkinter as tk
from tkinter import ttk, messagebox

data_transaksi = []

def update_pengerjaan():

    if jenis.get() in ["Bedcover", "Selimut"]:

        combo_pengerjaan["values"] = [
            "Regular (2 hari)",
            "Express (24 jam)"
        ]

    else:
        layanan = combo_layanan.get()

        if layanan == "Cuci Kering Lipat":
            combo_pengerjaan["values"] = [
                "Regular (1 hari)",
                "Express (6 jam)"
            ]

        elif layanan == "Hanya Setrika":
            combo_pengerjaan["values"] = [
                "Regular (1 hari)",
                "Express (6 jam)"
            ]

        elif layanan == "Cuci dan Setrika":
            combo_pengerjaan["values"] = [
                "Regular (2 hari)",
                "Express (24 jam)",
                "Express (6 jam)",
                "Express (3 jam)"
            ]

    combo_pengerjaan.set("")

def hitung_laundry():

    try:
        nama = entry_nama.get()
        berat = float(entry_berat.get())

        layanan = combo_layanan.get()
        pengerjaan_biasa = combo_pengerjaan.get()

        if nama == "":
            messagebox.showwarning(
                "Peringatan",
                "Nama belum diisi"
            )
            return

        total = 0
        detail = ""

        # =====================
        # PAKAIAN BIASA
        # =====================

        if jenis.get() == "Pakaian":            
            if berat <= 0:
                messagebox.showwarning(
                    "Peringatan",
                    "Masukkan berat pakaian biasa"
                )
                return
            if layanan == "Cuci Kering Lipat":

                if pengerjaan_biasa == "Regular (1 hari)":
                    harga = 6000
                    waktu = "1 hari"

                else:
                    harga = 10000
                    waktu = "6 jam"

            elif layanan == "Hanya Setrika":

                if pengerjaan_biasa == "Regular (1 hari)":
                    harga = 5000
                    waktu = "1 hari"

                else:
                    harga = 8000
                    waktu = "6 jam"

            elif layanan == "Cuci dan Setrika":

                if pengerjaan_biasa == "Regular (2 hari)":
                    harga = 8000
                    waktu = "2 hari"

                elif pengerjaan_biasa == "Express (24 jam)":
                    harga = 12000
                    waktu = "24 jam"

                elif pengerjaan_biasa == "Express (6 jam)":
                    harga = 20000
                    waktu = "6 jam"

                else:
                    harga = 25000
                    waktu = "3 jam"

            hasil = harga * berat

            total += hasil

            detail += (
                f"Pakaian Biasa\n"
                f"{berat} kg x Rp{harga:,}"
                f" = Rp{hasil:,.0f}\n"
            )

        # =====================
        # BEDCOVER
        # =====================

        if jenis.get() == "Bedcover":
            if berat <= 0:
                messagebox.showwarning(
                    "Peringatan",
                    "Masukkan berat bedcover"
                )
                return
            
            if combo_pengerjaan.get() == "Regular (2 hari)":
                harga = 25000
                waktu = "2 hari"

            else:
                harga = 30000
                waktu = "24 jam"

            hasil = harga * berat

            total += hasil

            detail += (
                f"Bedcover\n"
                f"{berat} kg x Rp{harga:,}"
                f" = Rp{hasil:,.0f}\n"
            )

        # =====================
        # SELIMUT
        # =====================

        if jenis.get() == "Selimut":
            if berat <= 0:
                messagebox.showwarning(
                    "Peringatan",
                    "Masukkan berat selimut"
                )
                return
            if combo_pengerjaan.get() == "Regular (2 hari)":

                harga = 10000
                waktu = "2 hari"

            else:

                harga = 15000
                waktu = "24 jam"

            hasil = harga * berat


            total += hasil

            detail += (
                f"Selimut\n"
                f"{berat} kg x Rp{harga:,}"
                f" = Rp{hasil:,.0f}\n"
            )

        # DISKON
        if total >= 200000:

            diskon = total * 0.15

        elif total >= 100000:

            diskon = total * 0.10

        elif total >= 50000:

            diskon = total * 0.05

        else:

            diskon = 0

        bayar = total - diskon

        output = (
            "====================\n"
            f"Nama : {nama}\n"
            f"Layanan : {layanan}\n"
            f"Pengerjaan : {combo_pengerjaan.get()}\n\n"

            f"{detail}\n"

            f"Total : Rp{total:,.0f}\n"
            f"Diskon : Rp{diskon:,.0f}\n"
            f"Bayar : Rp{bayar:,.0f}\n"
            "====================\n\n"
        )

        box_detail.insert(
            tk.END,
            output
        )

        data_transaksi.append(bayar)

        label_total.config(
            text=f"Total Pemasukan : Rp{sum(data_transaksi):,.0f}"
        )

    except:
        messagebox.showerror(
            "Error",
            "Berat harus berupa angka"
        )

def reset():

    entry_nama.delete(0, tk.END)
    entry_berat.delete(0, tk.END)

    combo_layanan.set("")
    combo_pengerjaan.set("")

    jenis.set("")

def hapus():

    box_detail.delete(
        "1.0",
        tk.END
    )

    data_transaksi.clear()

    label_total.config(
        text="Total Pemasukan : Rp0"
    )

# =====================
# GUI
# =====================

root = tk.Tk()

root.title("Aplikasi Laundry")
root.geometry("600x650")

tk.Label(
    root,
    text="APLIKASI MANAJEMEN LAUNDRY",
    font=("Arial",14,"bold")
).pack(pady=10)

frame = tk.Frame(root)
frame.pack()

tk.Label(
    frame,
    text="Nama Pelanggan"
).grid(row=0,column=0)

entry_nama = tk.Entry(frame)
entry_nama.grid(row=0,column=1)

tk.Label(
    frame,
    text="Berat (Kg)"
).grid(row=1, column=0)

entry_berat = tk.Entry(frame)
entry_berat.grid(row=1, column=1)

tk.Label(
    frame,
    text="Layanan"
).grid(row=6,column=0)

combo_layanan = ttk.Combobox(
    frame,
    values=[
        "Cuci Kering Lipat",
        "Hanya Setrika",
        "Cuci dan Setrika"
    ]
)
combo_layanan.grid(row=2,column=1)

combo_layanan.bind(
    "<<ComboboxSelected>>",
    lambda e:update_pengerjaan()
)

jenis = tk.StringVar(value="")

tk.Radiobutton(
    frame,
    text="Pakaian Biasa",
    variable=jenis,
    value="Pakaian",
    command=update_pengerjaan
).grid(row=3,column=0,sticky="w")

tk.Radiobutton(
    frame,
    text="Bedcover",
    variable=jenis,
    value="Bedcover",
    command=update_pengerjaan
).grid(row=4,column=0,sticky="w")

tk.Radiobutton(
    frame,
    text="Selimut",
    variable=jenis,
    value="Selimut",
    command=update_pengerjaan
).grid(row=5,column=0,sticky="w")

tk.Label(
    frame,
    text="Pengerjaan Pakaian"
).grid(row=6,column=0)

combo_pengerjaan = ttk.Combobox(frame)

combo_pengerjaan.grid(row=6,column=1)

tk.Button(
    root,
    text="Hitung Laundry",
    width=20,
    command=hitung_laundry
).pack(pady=10)

tk.Button(
    root,
    text="Reset",
    width=20,
    command=reset
).pack()

tk.Button(
    root,
    text="Hapus Detail",
    width=20,
    command=hapus
).pack(pady=5)

box_detail = tk.Text(
    root,
    width=65,
    height=18
)

box_detail.pack(pady=10)

label_total = tk.Label(
    root,
    text="Total Pemasukan : Rp0",
    font=("Arial",11,"bold")
)

label_total.pack()

root.mainloop()