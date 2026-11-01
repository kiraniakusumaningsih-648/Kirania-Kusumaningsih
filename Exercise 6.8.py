pet1 = {
    'animal': 'Anjing',
    'owner': 'Kirania'
}

pet2 = {
    'animal': 'Kucing',
    'owner': 'Fadlila'
}

pet3 = {
    'animal': 'Kelinci',
    'owner': 'Rut'
}

pet4 = {
    'animal': 'Hamster',
    'owner': 'Luthfi'
}

pets = [pet1, pet2, pet3, pet4]

for pet in pets:
    print("Jenis hewan:", pet['animal'])
    print("Nama pemilik:", pet['owner'])
    print()