rivers = {
    'nil': 'mesir',
    'amazon': 'brasil',
    'yangtze': 'tiongkok'
}

# Menampilkan kalimat tentang setiap sungai
for river, country in rivers.items():
    print(f"Sungai {river.title()} mengalir melalui negara {country.title()}.")

print("\nNama-nama sungai:")

# Menampilkan nama setiap sungai
for river in rivers.keys():
    print(river.title())

print("\nNama-nama negara:")

# Menampilkan nama setiap negara
for country in rivers.values():
    print(country.title())