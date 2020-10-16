file_path = 'textfiles/programming_poll.txt'

print('Please enter completed after all the persons have taken poll.')
while True:
    name = input('please enter your name: ')
    if name.lower() == 'completed':
        break
    else:
        poll = input(f'Hii {name.title()}! can you please tell us why you like programming??: ')
        with open(file_path,'a') as file_object:
            file_object.write(f"{name.title()} likes programming because of the following reasons: \n")
            file_object.write(f"\t\t\t\t>{poll}\n")


