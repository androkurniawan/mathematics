import math

# x = 5

# if x > 9:
#     print("Sangat bagus")
# elif x > 8:
#     print("Bagus")
# elif x > 6:
#     print("Biasa")
# else:
#     print("Gagal")



# # volume balok
# p = 2
# l = 3
# t = 4

# V = p * l * t
# print("Volume balok =", V)

# import math
# print("nilai pi = ", math.pi)

# a = float(input("Masukan angka pertama ="))        
# b = input("Masukan angka kedua =")
# c = input("Masukan angka ketiga =")

# ratarata = (a + b + c)/3

# print("Rata-ratanya adalah = ", ratarata)

# print("Nilai pi =", math.pi)


# usia = 20

# if usia < 5:
#     print("Anda adalah bayi")
# elif usia < 12:
#     print("Anda adalah anak-anak")
# elif usia < 18:
#     print("Anda adalah Remaja")
# else:
#     print("Anda Dewasa")

nama = input("Siapa nama Anda? ")
kelahiran = int(input("Tahun berapa Anda lahir? "))

if 1944 <= kelahiran <= 1964:
    print(nama, "Anda adalah generasi Baby Boomer")
elif 1965 <= kelahiran <= 1979:
    print(nama, "Anda adalah generasi X")
elif 1980 <= kelahiran <= 1994:
    print(nama, "Anda adalah generasi Y")
elif 1995 <= kelahiran <=  2015:
    print(nama, "Anda adalah generasi Z")
elif kelahiran >= 2016:
    print(nama, "Anda adalah generasi Alfa")
else:
    print("Masukkan kelahiran Anda dengan benar")


