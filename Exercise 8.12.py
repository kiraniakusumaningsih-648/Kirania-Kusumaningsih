def make_sandwich(*topping):
    print("\nPesanan sandwich:")
    for bahan in topping:
        print("- " + bahan)


make_sandwich("Keju", "Selada", "Tomat")

make_sandwich("Ayam", "Keju")

make_sandwich("Daging", "Telur", "Mayones", "Selada", "Tomat")