import json

file_name = 'favouritenumber.json'
with open(file_name) as f:
    fav_num = json.load(f)

print(f"I know your Favourite number that is {fav_num}")