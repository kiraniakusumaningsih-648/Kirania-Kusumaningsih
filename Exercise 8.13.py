def build_profile(first, last, **user_info):
    profile = {
        "first_name": first,
        "last_name": last
    }

    for key, value in user_info.items():
        profile[key] = value

    return profile


profil_saya = build_profile(
    "Kim",
    "Mingyu",
    usia=29,
    hobi="Bermain musik",
    pekerjaan="Penyanyi"
)

for key, value in profil_saya.items():
    print(key, ":", value)