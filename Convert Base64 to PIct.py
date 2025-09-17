import base64

with open("hasil_base64.txt", "r") as f:
    encoded_str = f.read()

decoded = base64.b64decode(encoded_str)

# Simpan lagi jadi gambar
with open("hasil_decode.jpg", "wb") as f:
    f.write(decoded)
