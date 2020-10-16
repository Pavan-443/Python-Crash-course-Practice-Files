sandwiches_orders = ['hog', 'won', 'emo', 'perlu']
finished_sandwiches = []
while sandwiches_orders:
    current_sandwich = sandwiches_orders.pop()
    print(f'I made your {current_sandwich}')
    finished_sandwiches.append(current_sandwich)
print('\nFollowing sandwiches are completed: ')
for sandwis in finished_sandwiches:
    print(f'\t\t\t\t\t\t\t\t   {sandwis}')