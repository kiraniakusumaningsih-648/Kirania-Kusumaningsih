favorite_languages = {
    'Fadlila': 'Python',
    'Luthfi': 'Java',
    'Kusuma': 'C++',
    'Auliya': 'JavaScript'
}

people = ['Fadlila', 'Luthfi', 'Kusuma', 'Auliya', 'Kirania', 'Geo']

for person in people:
    if person in favorite_languages:
        print(f"Terima kasih {person}, sudah mengisi jajak pendapat.")
    else:
        print(f"Halo {person}, silakan ikuti jajak pendapat bahasa pemrograman favorit.")