
class Restoran:
    def __init__(self, nama_restoran, jenis_masakan):
        self.nama_restoran = nama_restoran
        self.jenis_masakan = jenis_masakan
        self.jumlah_pelanggan = 0

    def deskripsikan_restoran(self):
        print(f"Nama restoran: {self.nama_restoran}")
        print(f"Jenis masakan: {self.jenis_masakan}")

    def buka_restoran(self):
        print(f"Restoran {self.nama_restoran} sedang buka!")

    def atur_jumlah_pelanggan(self, jumlah):
        self.jumlah_pelanggan = jumlah

    def tambah_jumlah_pelanggan(self, jumlah):
        self.jumlah_pelanggan += jumlah


restoran = Restoran("Sejahtera", "Masakan Indonesia")

print("Jumlah pelanggan awal:", restoran.jumlah_pelanggan)

restoran.jumlah_pelanggan = 25
print("Jumlah pelanggan setelah diubah:", restoran.jumlah_pelanggan)

restoran.atur_jumlah_pelanggan(50)
print("Jumlah pelanggan setelah menggunakan method:", restoran.jumlah_pelanggan)

restoran.tambah_jumlah_pelanggan(15)
print("Jumlah pelanggan setelah ditambahkan:", restoran.jumlah_pelanggan)