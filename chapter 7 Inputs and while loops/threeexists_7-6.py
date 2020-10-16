toppings = ''
active = True
while active:
    prompt = '\nplease enter the toppings you want to add'
    prompt += "\n{If you are done please enter 'quit'}: "
    toppings = input(prompt).lower()
    if toppings.upper() == 'QUIT':
        print('\nok, all your toppings will be added...')
        active = False
    elif toppings == 'quit':
        break
    elif toppings != 'quit:':
        print(f"Ok Your Topping,{toppings} will be added")