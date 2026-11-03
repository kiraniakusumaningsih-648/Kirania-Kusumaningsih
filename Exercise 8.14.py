def make_car(manufacturer, model, **car_info):
    car = {
        "manufacturer": manufacturer,
        "model": model
    }

    for key, value in car_info.items():
        car[key] = value

    return car


mobil = make_car(
    "Subaru",
    "Outback",
    color="Blue",
    tow_package=True
)

for key, value in mobil.items():
    print(key, ":", value)