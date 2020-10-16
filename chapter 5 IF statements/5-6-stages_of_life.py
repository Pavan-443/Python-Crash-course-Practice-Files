age = int(input('age:'))
if age < 2:
	print('The Person is a Baby')
elif age < 4:
	print('The Person is a Toddler')
elif age < 13:
	print('The Person is a Kid')
elif age < 20:
	print('The person is a Teenager')
elif age < 65:
	print('The person is an Adult')
else:
	print('The person is an Elder')