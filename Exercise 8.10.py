def send_messages(pesan, sent_messages):
    while pesan:
        pesan_sekarang = pesan.pop()
        print(pesan_sekarang)
        sent_messages.append(pesan_sekarang)


daftar_pesan = [
    "Selamat pagi!",
    "Apa kabar hari ini?",
    "Tetap semangat belajar!",
    "Jangan menyerah!",
    "Semoga harimu menyenangkan!"
]

sent_messages = []

send_messages(daftar_pesan, sent_messages)

print("\nDaftar pesan:")
print(daftar_pesan)

print("\nDaftar pesan terkirim:")
print(sent_messages)