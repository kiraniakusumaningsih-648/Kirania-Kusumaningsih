sandwich_orders = ['tuna', 'pastrami', 'ayam', 'pastrami', 'keju', 'pastrami', 'daging sapi']

finished_sandwiches = []

print("Maaf, deli kehabisan sandwich pastrami.")

while 'pastrami' in sandwich_orders:
    sandwich_orders.remove('pastrami')

while sandwich_orders:
    current_sandwich = sandwich_orders.pop()

    print(f"Saya sudah membuat sandwich {current_sandwich} Anda.")

    finished_sandwiches.append(current_sandwich)

print("\nSandwich yang sudah selesai dibuat:")

for sandwich in finished_sandwiches:
    print(f"- Sandwich {sandwich}")