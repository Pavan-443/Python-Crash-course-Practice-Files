favorite_places = {
    'pavan': ['india', 'kalikiri', 'markapur'],
    'mahesh': ['IIT hyd college','navodaya school'],
    'ramanamma': ['tirupati']
}

for name, favorite_place in favorite_places.items():
    print(f"\nHii {name.title()}!")
    if len(favorite_place) == 1:
        for place in favorite_place:
            print(f"{name.title()}, It seems your favourite place is {place}")
    if len(favorite_place) >1:
        print(f"{name.title()}, It seems your favourite places are: ")
        for place in favorite_place:
            print(f"\t\t\t\t\t\t\t\t\t{place.title()}")
