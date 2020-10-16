places = {}
prompt = 'you could visit one place in the world, where would you go? '
active = True
while active:
    name = input('Please enter your name: ')
    place = input(prompt)
    places[name] = place
    repeat = input('Do you want to give poll to your friend or any other person?(yes/no): ')
    if repeat.lower() == 'no':
        active = False

print('\n----Poll Results----')
for key, value in places.items():
    print(f"{key.title()}'s Dream vacation place is {value.title()}")