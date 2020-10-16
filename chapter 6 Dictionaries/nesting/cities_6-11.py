city1 = {
    'name': 'hyderabad',
    'population': '68.1 lakhs',
    'fact': '''It is very well know for its "Hyderabadi Biryani"'''
}

city2 = {
    'name': 'agra',
    'population': '22 lakhs',
    'fact': '''It one of the worlds' seven wonders, Taj mahal is located here.'''
}

city3 = {
    'name': 'jhansi',
    'population': '5.07 lakhs',
    'fact': '''It is one of the Ancient cities.'''
}

cities = [city1, city2, city3]

for city in cities:
    print(f"\n{city['name'].title()}:")
    print('This city is located in India')
    print(f"Population of {city['name'].title()} is {city['population']}")
    print(f"A fact about {city['name'].title()} is that {city['fact']}")