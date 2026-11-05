class Restoran:
    def __init__(self, nama_restoran, jenis_masakan):
        self.nama_restoran = nama_restoran
        self.jenis_masakan = jenis_masakan

    def deskripsikan_restoran(self):
        print(f"Nama restoran: {self.nama_restoran}")
        print(f"Jenis masakan: {self.jenis_masakan}")

    def buka_restoran(self):
        print(f"Restoran {self.nama_restoran} sedang buka!")


restoran = Restoran("Sejahtera", "Masakan Indonesia")

print(restoran.nama_restoran)
print(restoran.jenis_masakan)

restoran.deskripsikan_restoran()
restoran.buka_restoran()