import json


filename = 'favouritenumber.json'

try:
    with open(filename) as f:
        fav_num = json.load(f)
except FileNotFoundError:
    fav_num = int(input("Enter your favourite number: "))
    with open(filename, 'w') as f:
        json.dump(fav_num, f)
        print(f'Ok I will Remember that your favourite number is {fav_num}')
else:
    print(f"Hey I know your favorite number that is {fav_num}")