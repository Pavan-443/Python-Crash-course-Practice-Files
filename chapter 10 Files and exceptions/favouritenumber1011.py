import json
filename = 'favouritenumber.json'

fav_num = int(input("Enter your favourite number: "))
with open(filename, 'w') as f:
    json.dump(fav_num, f)
