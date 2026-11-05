import random

daftar_undian = [
    1, 2, 3, 4, 5, 6, 7, 8, 9, 10,
    "A", "B", "C", "D", "E"
]

my_ticket = [3, "B", 8, "D"]

jumlah_percobaan = 0

while True:
    nomor_pemenang = random.sample(daftar_undian, 4)
    jumlah_percobaan += 1

    if set(nomor_pemenang) == set(my_ticket):
        break

print("Nomor tiket saya:", my_ticket)
print("Nomor pemenang:", nomor_pemenang)
print("Tiket berhasil menang!")
print(f"Jumlah percobaan sampai menang: {jumlah_percobaan} kali")