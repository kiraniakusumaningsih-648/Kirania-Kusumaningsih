import random

daftar_undian = [
    1, 2, 3, 4, 5, 6, 7, 8, 9, 10,
    "A", "B", "C", "D", "E"
]

nomor_pemenang = random.sample(daftar_undian, 4)

print("Nomor undian yang terpilih:")
print(nomor_pemenang)

print("Tiket yang memiliki 4 angka atau huruf tersebut memenangkan hadiah!")