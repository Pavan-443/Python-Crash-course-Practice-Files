def sandwich_toppings(*toppings):
    """collects info on toppings that user needs on sandwich
    and prints what he has ardererd"""
    print(f'following are the toppings you have requested on sandwich(es): ')
    for topping in toppings:
        print(f'-{topping}')

print(f'\n')
sandwich_toppings('mirchi', 'ahf', 'lkasfd')
print(f'\n')
sandwich_toppings('lkjafds', 'lkjasdf', 'lakjf')
print(f'\n')
sandwich_toppings('lkjsa', 'kfla', 'lkaj')