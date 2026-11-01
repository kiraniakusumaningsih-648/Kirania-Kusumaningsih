nama = 'Kenta'

print("Pengujian kesamaan string:")
print(nama == 'Kenta')
print(nama == 'Rara')

print("\nPengujian ketidaksamaan string:")
print(nama != 'Rara')
print(nama != 'Kenta')

print("\nPengujian menggunakan lower():")
print(nama.lower() == 'kenta')
print(nama.lower() == 'KENTA')

angka = 20

print("\nPengujian perbandingan angka:")
print(angka == 20)
print(angka != 20)
print(angka > 10)
print(angka < 10)
print(angka >= 20)
print(angka <= 10)

print("\nPengujian menggunakan and:")
print(angka > 10 and angka < 30)
print(angka > 30 and angka < 50)

print("\nPengujian menggunakan or:")
print(angka > 30 or angka == 20)
print(angka > 30 or angka < 10)

buah = ['Apel', 'Jeruk', 'Mangga']

print("\nPengujian data dalam daftar:")
print('Apel' in buah)
print('Pisang' in buah)

print("\nPengujian data yang tidak ada dalam daftar:")
print('Pisang' not in buah)
print('Apel' not in buah)