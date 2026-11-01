# Membuat daftar tempat yang ingin dikunjungi
tempat = ['Jepang', 'Swiss', 'Korea Selatan', 'Turki', 'Italia']

# Menampilkan daftar asli
print("Daftar tempat asli:")
print(tempat)

# Mengurutkan secara alfabetis tanpa mengubah daftar asli
print("\nUrutan alfabetis:")
print(sorted(tempat))

# Membuktikan daftar asli tidak berubah
print("\nDaftar asli:")
print(tempat)

# Mengurutkan secara alfabetis terbalik
print("\nUrutan alfabetis terbalik:")
print(sorted(tempat, reverse=True))

# Membuktikan daftar asli tidak berubah
print("\nDaftar asli:")
print(tempat)

# Membalik urutan daftar
tempat.reverse()
print("\nSetelah menggunakan reverse():")
print(tempat)

# Mengembalikan ke urutan semula
tempat.reverse()
print("\nKembali ke urutan semula:")
print(tempat)

# Mengurutkan daftar secara alfabetis
tempat.sort()
print("\nSetelah menggunakan sort():")
print(tempat)

# Mengurutkan daftar secara alfabetis terbalik
tempat.sort(reverse=True)
print("\nSetelah menggunakan sort(reverse=True):")
print(tempat)