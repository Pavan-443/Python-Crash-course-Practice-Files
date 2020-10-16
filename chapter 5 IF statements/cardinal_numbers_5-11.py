numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9]
for num in numbers:
	if num == 1:
		cardinal = f'{num}st'
	elif num == 2:
		cardinal = f'{num}nd'
	elif num == 3:
		cardinal = f'{num}rd'
	else:
		cardinal = f'{num}th'
	print(f"cardinal of {num} is {cardinal}")