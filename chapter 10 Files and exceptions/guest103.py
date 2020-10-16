file_location = 'textfiles/guests.txt'

name = input('Please enter your name: ')

with open(file_location, 'w') as file_object:
    file_object.write(f"Guest name is {name.title()}")