while True:
    topping = input("Masukkan topping pizza (ketik 'quit' untuk selesai): ")

    if topping == 'quit':
        break
    else:
        print(f"Saya akan menambahkan {topping} ke pizza Anda.")

print("Pesanan pizza selesai!")