import random

class Dadu:
    def __init__(self, sisi=6):
        self.sisi = sisi

    def lempar_dadu(self):
        angka = random.randint(1, self.sisi)
        print(angka)


dadu6 = Dadu()
dadu10 = Dadu(10)
dadu20 = Dadu(20)

print("Hasil lemparan dadu 6 sisi:")
for i in range(10):
    dadu6.lempar_dadu()

print("\nHasil lemparan dadu 10 sisi:")
for i in range(10):
    dadu10.lempar_dadu()

print("\nHasil lemparan dadu 20 sisi:")
for i in range(10):
    dadu20.lempar_dadu()