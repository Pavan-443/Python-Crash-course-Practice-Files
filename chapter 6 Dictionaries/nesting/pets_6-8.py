pet1 = {
    'animal': 'dog',
    'name': 'snoopy',
    'owner name': 'mahesh'
}

pet2 = {
    'animal': 'parrot',
    'name': 'mintu',
    'owner name': 'pavan'
}

pet3 = {
    'animal': 'rabbit',
    'name': 'raju',
    'owner name': 'ramanamma'
}

pet4 = {
    'animal': 'peacock',
    'name': 'chintu',
    'owner name': 'venkateswarlu'
}

pet5 = {
    'animal': 'dove',
    'name': 'chitragreevam',
    'owner name': 'bhavya'
}

pets = [pet1, pet2, pet3, pet4, pet5]

for pet in pets:
    print(f"\nAnimal is {pet['animal'].title()}")
    print(f"Animal name is {pet['name'].title()}")
    print(f"{pet['name'].title()}'s owner is {pet['owner name'].title()}")