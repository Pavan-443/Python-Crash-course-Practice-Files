import json

file_name = 'textfiles/numbers.json'
with open(file_name) as f:
    numbers = json.load(f)

print(numbers)