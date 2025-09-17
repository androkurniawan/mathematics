import base64

# Baca foto sebagai binary
with open("contoh.png", "rb") as f:
    encoded = base64.b64encode(f.read())

# Ubah hasilnya jadi string (utf-8) supaya bisa disimpan/ditampilkan
encoded_str = encoded.decode("utf-8")

# Cetak sebagian hasil base64
print(encoded_str[:200])

# Simpan ke file txt
with open("hasil_base64.txt", "w") as f:
    f.write(encoded_str)
