daftar_tamu = ["Jaemin", "Jeno", "Mark", "Mingyu", "Kai", "Suho", "Jisung"]

# Memberitahu bahwa hanya dua orang yang bisa diundang
print("Maaf, saya hanya bisa mengundang dua orang untuk makan malam.")

# Menghapus tamu satu per satu
tamu_dihapus = daftar_tamu.pop()
print("Maaf " + tamu_dihapus + ", kamu tidak bisa diundang.")

tamu_dihapus = daftar_tamu.pop()
print("Maaf " + tamu_dihapus + ", kamu tidak bisa diundang.")

tamu_dihapus = daftar_tamu.pop()
print("Maaf " + tamu_dihapus + ", kamu tidak bisa diundang.")

tamu_dihapus = daftar_tamu.pop()
print("Maaf " + tamu_dihapus + ", kamu tidak bisa diundang.")

tamu_dihapus = daftar_tamu.pop()
print("Maaf " + tamu_dihapus + ", kamu tidak bisa diundang.")

# Mencetak dua tamu yang masih diundang
print("\nHalo " + daftar_tamu[0] + ", kamu tetap diundang.")
print("Halo " + daftar_tamu[1] + ", kamu tetap diundang.")

# Menghapus dua nama terakhir dari daftar
del daftar_tamu[0]
del daftar_tamu[0]

# Menampilkan daftar tamu kosong
print("\nDaftar tamu sekarang:", daftar_tamu)