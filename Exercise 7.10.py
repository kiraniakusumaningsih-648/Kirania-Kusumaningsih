responses = {}

polling_active = True

while polling_active:
    name = input("Siapa nama Anda? ")
    vacation = input("Jika Anda bisa mengunjungi satu tempat di dunia, ke mana Anda akan pergi? ")

    responses[name] = vacation

    repeat = input("Apakah ada orang lain yang ingin menjawab? (ya/tidak) ")

    if repeat == 'tidak':
        polling_active = False

print("\n--- HASIL SURVEI LIBURAN IMPIAN ---")

for name, vacation in responses.items():
    print(f"{name} ingin berlibur ke {vacation}.")