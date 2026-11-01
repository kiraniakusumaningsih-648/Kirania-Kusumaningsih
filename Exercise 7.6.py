# Versi 1: Menggunakan kondisi while
print("VERSI 1: KONDISI WHILE")

pesan = ""

while pesan != 'keluar':
    pesan = input("Masukkan nama (atau ketik 'keluar' untuk berhenti): ")

    if pesan != 'keluar':
        print(f"Halo, {pesan}!")


# Versi 2: Menggunakan variabel aktif
print("\nVERSI 2: VARIABEL AKTIF")

aktif = True

while aktif:
    pesan = input("Masukkan nama (atau ketik 'keluar' untuk berhenti): ")

    if pesan == 'keluar':
        aktif = False
    else:
        print(f"Halo, {pesan}!")


# Versi 3: Menggunakan break
print("\nVERSI 3: PERINTAH BREAK")

while True:
    pesan = input("Masukkan nama (atau ketik 'keluar' untuk berhenti): ")

    if pesan == 'keluar':
        break
    else:
        print(f"Halo, {pesan}!")