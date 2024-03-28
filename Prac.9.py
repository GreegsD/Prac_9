class City:
    def __init__(self, city_name, country):
        self.city_name = city_name
        self.country = country

    def message(self):
        return f"Це місто {self.city_name}, яке знаходиться в країні {self.country}"


class Country:
    def __init__(self, country_name):
        self.country_name = country_name


class Europe(Country):
    def __init__(self, country_name):
        super().__init__(country_name)


class Australia(Country):
    def __init__(self, country_name):
        super().__init__(country_name)


europe_cities = [
    City("Страсбург", Europe("Франція")),
    City("Тулуза", Europe("Франція")),
    City("Марсель", Europe("Франція")),
    City("Бірмінгем", Europe("Велика Британія")),
    City("Манчестер", Europe("Велика Британія"))
]

australia_cities = [
    City("Канберра", Australia("Австралія")),
    City("Сідней", Australia("Австралія")),
    City("Мельбурн", Australia("Австралія"))
]

print("Повідомлення для міст Європи:")
for city in europe_cities:
    print(city.message())

print("\nПовідомлення для міст Австралії:")
for city in australia_cities:
    print(city.message())
