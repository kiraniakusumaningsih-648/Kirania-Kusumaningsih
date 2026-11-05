
class Pengguna:
    def __init__(self, nama_depan, nama_belakang, umur, alamat, pekerjaan, hobi):
        self.nama_depan = nama_depan
        self.nama_belakang = nama_belakang
        self.umur = umur
        self.alamat = alamat
        self.pekerjaan = pekerjaan
        self.hobi = hobi
        self.login_attempts = 0

    def deskripsikan_pengguna(self):
        print("Informasi Pengguna:")
        print(f"Nama depan: {self.nama_depan}")
        print(f"Nama belakang: {self.nama_belakang}")
        print(f"Umur: {self.umur} tahun")
        print(f"Alamat: {self.alamat}")
        print(f"Pekerjaan: {self.pekerjaan}")
        print(f"Hobi: {self.hobi}")

    def sapa_pengguna(self):
        print(f"Halo, {self.nama_depan} {self.nama_belakang}! Selamat datang!")

    def increment_login_attempts(self):
        self.login_attempts += 1

    def reset_login_attempts(self):
        self.login_attempts = 0


pengguna = Pengguna("Kirania", "Kusuma", 18, "Surakarta", "Mahasiswa", "Mendengarkan musik")

pengguna.increment_login_attempts()
pengguna.increment_login_attempts()
pengguna.increment_login_attempts()
pengguna.increment_login_attempts()
pengguna.increment_login_attempts()

print("Jumlah percobaan login:", pengguna.login_attempts)

pengguna.reset_login_attempts()

print("Jumlah percobaan login setelah direset:", pengguna.login_attempts)