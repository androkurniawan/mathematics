data = {
    "M001": {
        "nama": "Andi",
        "prodi": "Matematika",
        "semester": 2,
        "ipk": 3.45
    },
    "M002": {
        "nama": "Budi",
        "prodi": "Statistika",
        "semester": 4,
        "ipk": 3.72
    },
    "M003": {
        "nama": "Citra",
        "prodi": "Aktuaria",
        "semester": 2,
        "ipk": 3.90
    },
    "M004": {
        "nama": "Dewi",
        "prodi": "Matematika",
        "semester": 6,
        "ipk": 3.90
    }
}

tambahan = {"M005": {
        "nama": "Putra",
        "prodi": "Fisika",
        "semester": 8,
        "ipk": 2.8}
    }

data.update(tambahan)

print(data)

# data --> NIM --> nama

# for item in data:
#     print(data[item]["nama"])