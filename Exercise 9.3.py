
class Pengguna:
    def __init__(self, nama_depan, nama_belakang, umur, alamat, pekerjaan, hobi):
        self.nama_depan = nama_depan
        self.nama_belakang = nama_belakang
        self.umur = umur
        self.alamat = alamat
        self.pekerjaan = pekerjaan
        self.hobi = hobi

    def deskripsikan_pengguna(self):
        print("Informasi Pengguna:")
        print(f"Nama depan: {self.nama_depan}")
        print(f"Nama belakang: {self.nama_belakang}")
        print(f"Umur: {self.umur} tahun")
        print(f"Alamat: {self.alamat}")
        print(f"Pekerjaan: {self.pekerjaan}")
        print(f"Hobi: {self.hobi}")
        print()

    def sapa_pengguna(self):
        print(f"Halo, {self.nama_depan} {self.nama_belakang}! Selamat datang!")
        print()


pengguna1 = Pengguna("Kirania", "Kusuma", 18, "Surakarta", "Mahasiswa", "Mendengarkan musik")
pengguna2 = Pengguna("Kim", "Mingyu", 20, "Bandung", "Mahasiswa", "Main musik")
pengguna3 = Pengguna("Chrisania", "Mareta", 15, "Jakarta", "Pelajar", "Menggambar")


pengguna1.deskripsikan_pengguna()
pengguna1.sapa_pengguna()

pengguna2.deskripsikan_pengguna()
pengguna2.sapa_pengguna()

pengguna3.deskripsikan_pengguna()
pengguna3.sapa_pengguna()