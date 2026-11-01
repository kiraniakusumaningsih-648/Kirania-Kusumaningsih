while True:
    age = input("Masukkan usia Anda (ketik 'quit' untuk selesai): ")

    if age == 'quit':
        break

    age = int(age)

    if age < 3:
        print("Tiket bioskop gratis.")
    elif age <= 12:
        print("Harga tiket bioskop adalah $10.")
    else:
        print("Harga tiket bioskop adalah $15.")

print("Terima kasih sudah menggunakan program ini!")