import json

file_name = 'textfiles/numbers.json'
numbers = [1, 2, 3, 4, 5, 6, 7]
with open(file_name, 'w') as f:
    json.dump(numbers, f)
