file_path = 'textfiles/pi_million_digits.txt'

with open(file_path) as file_object:
    content = file_object.read()

print(content.strip())