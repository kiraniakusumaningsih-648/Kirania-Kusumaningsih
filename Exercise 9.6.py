
class Restoran:
    def __init__(self, nama_restoran, jenis_masakan):
        self.nama_restoran = nama_restoran
        self.jenis_masakan = jenis_masakan

    def deskripsikan_restoran(self):
        print(f"Nama restoran: {self.nama_restoran}")
        print(f"Jenis masakan: {self.jenis_masakan}")

    def buka_restoran(self):
        print(f"Restoran {self.nama_restoran} sedang buka!")


class KedaiEsKrim(Restoran):
    def __init__(self, nama_restoran, jenis_masakan):
        super().__init__(nama_restoran, jenis_masakan)
        self.rasa_es_krim = ["Cokelat", "Vanila", "Stroberi", "Matcha", "Mangga"]

    def tampilkan_rasa(self):
        print("Daftar rasa es krim:")
        for rasa in self.rasa_es_krim:
            print(f"- {rasa}")


kedai = KedaiEsKrim("Es Krim Bahagia", "Es Krim")

kedai.deskripsikan_restoran()
kedai.tampilkan_rasa()