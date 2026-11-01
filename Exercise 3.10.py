
# Membuat daftar nama gunung
gunung = ['Everest', 'Fuji', 'Kilimanjaro']

# 1. Menggunakan append() untuk menambahkan data
gunung.append('Alpen')
print("Setelah menggunakan append():")
print(gunung)

# 2. Menggunakan insert() untuk menambahkan data pada posisi tertentu
gunung.insert(1, 'Himalaya')
print("\nSetelah menggunakan insert():")
print(gunung)

# 3. Menggunakan remove() untuk menghapus data berdasarkan nama
gunung.remove('Fuji')
print("\nSetelah menggunakan remove():")
print(gunung)

# 4. Menggunakan del untuk menghapus data berdasarkan indeks
del gunung[2]
print("\nSetelah menggunakan del:")
print(gunung)

# 5. Menggunakan pop() untuk menghapus data terakhir
gunung_dihapus = gunung.pop()
print("\nSetelah menggunakan pop():")
print("Gunung yang dihapus:", gunung_dihapus)
print(gunung)

# Menambahkan data kembali
gunung.append('Fuji')
gunung.append('Andes')

# 6. Menggunakan sorted() untuk mengurutkan secara alfabetis
print("\nUrutan alfabetis:")
print(sorted(gunung))

# 7. Menggunakan sorted() untuk urutan alfabetis terbalik
print("\nUrutan alfabetis terbalik:")
print(sorted(gunung, reverse=True))

# 8. Menggunakan reverse() untuk membalik urutan daftar
gunung.reverse()
print("\nSetelah menggunakan reverse():")
print(gunung)

# 9. Menggunakan sort() untuk mengurutkan secara alfabetis
gunung.sort()
print("\nSetelah menggunakan sort():")
print(gunung)

# 10. Menggunakan sort(reverse=True) untuk urutan terbalik
gunung.sort(reverse=True)
print("\nSetelah menggunakan sort(reverse=True):")
print(gunung)

# 11. Menggunakan len() untuk menghitung jumlah data
print("\nJumlah gunung dalam daftar:")
print(len(gunung))
