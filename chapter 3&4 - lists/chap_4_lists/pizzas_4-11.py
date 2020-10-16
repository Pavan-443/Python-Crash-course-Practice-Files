cool_drinks = ['mazaa', 'sprite', 'limca']
for drink in cool_drinks:
	print(f'I like {drink.title()}!')
print('\nI love cool drinks! ecspecially during summer\n\nI love the cool drinks which are chill and tasty especially mango flavoured\n\nyou know what even without any fruit, still I like sprite which is very chill to drink')
friend_drinks = cool_drinks[:]
cool_drinks.append('fizz')
friend_drinks.append('pepsi')
print('\nmy favourite drinks are:')
for drink in cool_drinks:
	print(f'\t\t\t\t\t\t{drink}')
print('\nmy friends favourite drinks are:')
for friend_drink in friend_drinks:
	print(f'\t\t\t\t\t\t{friend_drink}')