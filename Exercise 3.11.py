# Membuat daftar nama gunung
gunung = ['Everest', 'Fuji', 'Kilimanjaro']

# Menampilkan daftar gunung
print("Daftar nama gunung:")
print(gunung)

# 1. Menghapus data berdasarkan indeks
del gunung[2]

print("\nSetelah menggunakan del:")
print(gunung)

# 2. Menghapus data terakhir
gunung_dihapus = gunung.pop()

print("\nSetelah menggunakan pop():")
print("Gunung yang dihapus:", gunung_dihapus)
print(gunung)

# 3. Menampilkan jumlah data
print("\nJumlah gunung dalam daftar:")
print(len(gunung))