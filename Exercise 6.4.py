glossary = {
    'variable': 'Tempat untuk menyimpan data.',
    'list': 'Digunakan untuk menyimpan beberapa data dalam satu variabel.',
    'dictionary': 'Struktur data yang menyimpan pasangan key dan value.',
    'loop': 'Digunakan untuk mengulang perintah beberapa kali.',
    'if statement': 'Digunakan untuk menjalankan perintah berdasarkan kondisi tertentu.',
    'string': 'Tipe data yang berisi kumpulan karakter atau teks.',
    'integer': 'Tipe data berupa bilangan bulat.',
    'float': 'Tipe data berupa bilangan desimal.',
    'boolean': 'Tipe data yang memiliki nilai True atau False.',
    'print': 'Perintah untuk menampilkan output ke layar.'
}

for word, meaning in glossary.items():
    print(word.title() + ":")
    print("  " + meaning + "\n")