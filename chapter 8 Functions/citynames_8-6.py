def city_country(city, country):
    """simply returns a string of city,country"""
    string = f"{city.title()}, {country.title()}"
    return string

print(city_country('Mumbai', 'india'))
print(city_country('delhi', 'india'))
print(city_country('new york', 'u.s.a'))