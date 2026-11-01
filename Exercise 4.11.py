pizza = ['Sosis', 'Keju', 'Ayam']

friend_pizzas = pizza[:]

pizza.append('Jamur')
friend_pizzas.append('Pepperoni')

print("Pizza favorit saya:")
for jenis in pizza:
    print(jenis)

print("\nPizza favorit teman saya:")
for jenis in friend_pizzas:
    print(jenis)