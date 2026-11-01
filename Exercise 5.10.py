current_users = ['Fadlila', 'Luthfi', 'Kusuma', 'Auliya', 'Andi']

new_users = ['FADLILA', 'Budi', 'LUTHFI', 'Siti', 'Rina']

current_users_lower = [user.lower() for user in current_users]

for new_user in new_users:
    if new_user.lower() in current_users_lower:
        print(f"Maaf, username {new_user} sudah digunakan. Silakan masukkan username lain.")
    else:
        print(f"Username {new_user} tersedia.")