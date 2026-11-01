makanan = ('Nasi Goreng', 'Ayam Goreng', 'Sate', 'Bakso', 'Mie Ayam')

print("Menu makanan restoran:")
for jenis in makanan:
    print(jenis)

print("\nMencoba mengubah salah satu menu:")

try:
    makanan[0] = 'Rendang'
except TypeError:
    print("Menu tidak dapat diubah karena tuple bersifat tetap.")

makanan = ('Nasi Goreng', 'Rendang', 'Sate', 'Soto', 'Mie Ayam')

print("\nMenu makanan setelah diperbarui:")
for jenis in makanan:
    print(jenis)