favorite_places = {
    'Kirania': ['Bali', 'Yogyakarta', 'Bandung'],
    'Fadlila': ['Pantai', 'Gunung'],
    'Rut': ['Jakarta', 'Malang', 'Surakarta']
}

for name, places in favorite_places.items():
    print("Tempat favorit", name, "adalah:")

    for place in places:
        print("-", place)

    print()