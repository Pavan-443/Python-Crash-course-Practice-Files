user_names = ['mahesh', 'pavan', 'venkateswarlu', 'ramanamma', 'admin']
for user_name in user_names:
	if user_name == 'admin':
		print(f'Hello {user_name.title()}, would you like to review status?')
	else:
		print(f'Hii {user_name.title()} thanks for logging in again')