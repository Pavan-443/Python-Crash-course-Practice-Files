print('The Deli has run out of Pastrami')
sandwiches_orders = ['hog', 'pastrami', 'won', 'pastrami', 'emo', 'perlu', 'pastrami']
while 'pastrami' in sandwiches_orders:
    sandwiches_orders.remove('pastrami')
finished_sandwiches = []
while sandwiches_orders:
    current_sandwich = sandwiches_orders.pop()
    print(f'I made your {current_sandwich}')
    finished_sandwiches.append(current_sandwich)
print('\nFollowing sandwiches are completed: ')
for sandwis in finished_sandwiches:
    print(f'\t\t\t\t\t\t\t\t   {sandwis}')