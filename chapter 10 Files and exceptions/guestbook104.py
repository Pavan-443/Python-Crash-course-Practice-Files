file_location = 'textfiles/guest_book.txt'

while True:
    name = input('Please enter your name: ')
    print(f'Hii {name}')
    with open(file_location, 'a') as file_object:
        file_object.write(f"{name.title()} has visited\n")
    prompt = input(f'Is there any one else who have to enter name??(yes/no) ')
    if prompt.lower == 'yes':
        pass
    if prompt.lower() == 'no':
        break
