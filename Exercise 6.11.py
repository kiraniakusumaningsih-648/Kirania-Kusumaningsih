cities = {
    'Jakarta': {
        'country': 'Indonesia',
        'population': '10,6 juta jiwa',
        'fact': 'Merupakan ibu kota terbesar di Indonesia.'
    },

    'Tokyo': {
        'country': 'Jepang',
        'population': '14 juta jiwa',
        'fact': 'Memiliki sistem transportasi kereta yang sangat maju.'
    },

    'Paris': {
        'country': 'Prancis',
        'population': '2,1 juta jiwa',
        'fact': 'Terkenal dengan Menara Eiffel.'
    }
}

for city, information in cities.items():
    print("Nama kota:", city)
    print("Negara:", information['country'])
    print("Jumlah penduduk:", information['population'])
    print("Fakta:", information['fact'])
    print()