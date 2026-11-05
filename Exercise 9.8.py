
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
        print(f"Nama: {self.nama_depan} {self.nama_belakang}")
        print(f"Umur: {self.umur} tahun")
        print(f"Alamat: {self.alamat}")
        print(f"Pekerjaan: {self.pekerjaan}")
        print(f"Hobi: {self.hobi}")


class Privileges:
    def __init__(self):
        self.privileges = [
            "Dapat menambahkan postingan",
            "Dapat menghapus postingan",
            "Dapat memblokir pengguna",
            "Dapat mengelola akun pengguna"
        ]

    def show_privileges(self):
        print("Hak istimewa administrator:")
        for hak in self.privileges:
            print(f"- {hak}")


class Admin(Pengguna):
    def __init__(self, nama_depan, nama_belakang, umur, alamat, pekerjaan, hobi):
        super().__init__(nama_depan, nama_belakang, umur, alamat, pekerjaan, hobi)
        self.privileges = Privileges()


admin = Admin("Kirania", "Kusuma", 18, "Surakarta", "Mahasiswa", "Mendengarkan musik")

admin.deskripsikan_pengguna()
admin.privileges.show_privileges()