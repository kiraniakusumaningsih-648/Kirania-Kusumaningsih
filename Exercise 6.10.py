favorite_numbers = {
    'Kirania': [30, 6, 8],
    'Fadlila': [8, 20, 5],
    'Luthfi': [10, 15, 25],
    'Kusuma': [5, 12, 17],
    'Auliya': [9, 18, 21]
}

for name, numbers in favorite_numbers.items():
    print("Angka favorit", name, "adalah:")

    for number in numbers:
        print("-", number)

    print()