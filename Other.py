buah = ["apel", "mangga", "jeruk", "melon", "lemon", "durian", "rambutan", "anggur",
        "strawberry", "salak", "apel", "melon", "anggur", "durian", "jeruk", "pepaya",
        "pisang", "kiwi", "nanas", "semangka", "manggis", "sirsak", "jambu", "alpukat",
        "ceri", "pepaya", "pisang", "apel", "melon", "anggur",  "leci", "kurma", "plum",
        "persik", "markisa", "belimbing", "kedondong", "buah naga", "duku", "pir", "apel",
        "durian", "jeruk", "mangga", "salak", "kiwi", "nanas", "semangka", "rambutan", "ceri"]

# def buah_buahan(buah):
#     hitung = 0
#     daftar = []

#     for name in buah:
#         if name not in daftar:
#             daftar.append(name)
#             hitung = hitung + 1
#     return hitung

for i in buah:

    hitung = 0

    for j in buah:
        if i == j:
            hitung = hitung + 1

    if hitung == 1:
        print(i)
print(hitung)
# print(buah_buahan(buah))