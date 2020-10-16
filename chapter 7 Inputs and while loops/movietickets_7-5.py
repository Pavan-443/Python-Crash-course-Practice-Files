prompt = 'please enter your age\nso that I can tell about your ticket price: '
age = int(input(prompt))
if age <= 3:
    print('Ticket is Free')
if age <=12:
    print('Ticket Fee is $10')
if age >12:
    print('Ticket Fee is $15')