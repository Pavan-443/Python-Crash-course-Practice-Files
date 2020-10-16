def print_citycountry(city, country, population=None):
    if population:
        string = f"{city}, {country}, Population -{population}"
    else:
        string = f"{city}, {country}"
    return string

