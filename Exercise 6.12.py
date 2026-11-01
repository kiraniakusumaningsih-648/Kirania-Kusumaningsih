person1 = {
    'first_name': 'Kirania',
    'last_name': 'Kusumaningsih',
    'age': 18,
    'city': 'Surakarta',
    'hobby': 'Mendengarkan musik',
    'favorite_food': 'Chicken Steak'
}

person2 = {
    'first_name': 'Fadlila Mutiara',
    'last_name': 'Aini',
    'age': 20,
    'city': 'Surakarta',
    'hobby': 'Memasak',
    'favorite_food': 'Seblak'
}

person3 = {
    'first_name': 'Rut',
    'last_name': 'Windi',
    'age': 18,
    'city': 'Surakarta',
    'hobby': 'Menonton film',
    'favorite_food': 'Bakso'
}

people = [person1, person2, person3]

for person in people:
    print("===== DATA DIRI =====")
    print("Nama lengkap:", person['first_name'], person['last_name'])
    print("Umur:", person['age'], "tahun")
    print("Kota:", person['city'])
    print("Hobi:", person['hobby'])
    print("Makanan favorit:", person['favorite_food'])
    print()