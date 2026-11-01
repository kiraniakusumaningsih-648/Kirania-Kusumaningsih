person1 = {
    'first_name': 'Kirania',
    'last_name': 'Kusumaningsih',
    'age': 18,
    'city': 'Surakarta'
}

person2 = {
    'first_name': 'Fadlila Mutiara',
    'last_name': 'Aini',
    'age': 20,
    'city': 'Surakarta'
}

person3 = {
    'first_name': 'Rut',
    'last_name': 'Windi',
    'age': 18,
    'city': 'Surakarta'
}

people = [person1, person2, person3]

for person in people:
    print("Nama depan:", person['first_name'])
    print("Nama belakang:", person['last_name'])
    print("Umur:", person['age'])
    print("Kota:", person['city'])
    print()