user_names = ['mahesh', 'pavan', 'venkateswarlu', 'ramanamma', 'admin']
for user_name in user_names:
	if user_name == 'admin':
		print(f'Hello {user_name.title()}, would you like to review status?')
	else:
		print(f'Hii {user_name.title()} thanks for logging in again')

if user_names:
	for user_name in user_names:
		if user_names == 'admin':
			print(f'Hello {user_name.title()}, would you like to review the status')
		else:
			print(f'Hii {user_name.title()}, Thanks for logging in again')
else:
	print('We need to have Usernames!')