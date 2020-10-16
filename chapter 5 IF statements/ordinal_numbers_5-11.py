numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9]

for num in numbers:
	if num == 1:
		ordinal = f'{num}st'
	elif num == 2:
		ordinal = f'{num}nd'
	elif num == 3:
		ordinal = f'{num}rd'
	else:
		ordinal = f'{num}th'
	print(f'ordinal of {num} is {ordinal}')