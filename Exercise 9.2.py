
class Restoran:
    def __init__(self, nama_restoran, jenis_masakan):
        self.nama_restoran = nama_restoran
        self.jenis_masakan = jenis_masakan

    def deskripsikan_restoran(self):
        print(f"Nama restoran: {self.nama_restoran}")
        print(f"Jenis masakan: {self.jenis_masakan}")
        print()

    def buka_restoran(self):
        print(f"Restoran {self.nama_restoran} sedang buka!")


restoran1 = Restoran("Sejahtera", "Masakan Indonesia")
restoran2 = Restoran("Sakura", "Masakan Jepang")
restoran3 = Restoran("Pizza Mantap", "Masakan Italia")

restoran1.deskripsikan_restoran()
restoran2.deskripsikan_restoran()
restoran3.deskripsikan_restoran()