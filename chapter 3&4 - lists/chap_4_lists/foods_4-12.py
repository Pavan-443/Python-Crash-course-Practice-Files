my_fav_foods = ['biryani', 'sambhar rice', 'mutton', 'fish']

friend_foods = ['chicken', 'veg','curries', 'cauli flower', 'mushrooms']

print('My favourite foods are:')
for my_food in my_fav_foods:
	print(f'\t\t\t\t\t\t{my_food.title()}')


print('''\nMy friend's favourite foods are:''')
for food in friend_foods:
	print(f'\t\t\t\t\t\t\t\t{food.title()}')