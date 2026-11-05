
class Mobil:
    def __init__(self, merek, model, tahun):
        self.merek = merek
        self.model = model
        self.tahun = tahun

    def deskripsikan_mobil(self):
        print(f"Mobil: {self.merek} {self.model}")
        print(f"Tahun: {self.tahun}")


class Baterai:
    def __init__(self, kapasitas=40):
        self.kapasitas = kapasitas

    def upgrade_baterai(self):
        if self.kapasitas != 65:
            self.kapasitas = 65
            print("Kapasitas baterai berhasil ditingkatkan menjadi 65 kWh.")

    def tampilkan_kapasitas(self):
        print(f"Kapasitas baterai: {self.kapasitas} kWh")

    def get_range(self):
        if self.kapasitas == 40:
            jarak = 150
        elif self.kapasitas == 65:
            jarak = 225
        else:
            jarak = 0

        print(f"Mobil dapat menempuh jarak sekitar {jarak} km.")


class MobilListrik(Mobil):
    def __init__(self, merek, model, tahun):
        super().__init__(merek, model, tahun)
        self.baterai = Baterai()


mobil = MobilListrik("Tesla", "Model S", 2024)

mobil.deskripsikan_mobil()

print("\nSebelum upgrade baterai:")
mobil.baterai.tampilkan_kapasitas()
mobil.baterai.get_range()

print("\nSetelah upgrade baterai:")
mobil.baterai.upgrade_baterai()
mobil.baterai.tampilkan_kapasitas()
mobil.baterai.get_range()