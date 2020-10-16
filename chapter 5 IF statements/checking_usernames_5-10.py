current_users = ['pavan', 'Mahesh', 'jayakar', 'advaith', 'Varshith']
new_users = ['Pavan', 'mahesh', 'varshith', 'rudheer', 'hari']

current_users2 = []
for name in current_users:
	current_users2.append(name.lower())

for name in new_users:
	if name.lower() in current_users2:
		print(f'{name} name is not available it is already taken, please take other username')
	else:
		print(f'{name} is available')