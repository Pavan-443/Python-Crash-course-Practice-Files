toppings = ''
while toppings.lower() != 'quit':
    prompt = '\nplease enter the toppings you want to add'
    prompt += "\n{If you are done please enter 'quit'}: "
    toppings = input(prompt).lower()
    print(f"Ok Your Topping,{toppings} will be added")
    if toppings == 'quit':
        print('\nok, all your toppings will be added...')
        break
