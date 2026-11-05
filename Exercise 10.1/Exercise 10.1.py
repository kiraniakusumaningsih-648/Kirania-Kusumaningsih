with open("learning_python.txt") as file:
    isi_file = file.read()

print("Membaca seluruh isi file:")
print(isi_file)


with open("learning_python.txt") as file:
    daftar_baris = file.readlines()

print("Membaca file menggunakan list dan perulangan:")
for baris in daftar_baris:
    print(baris.strip())