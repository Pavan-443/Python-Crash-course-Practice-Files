cubes = []
numbers = list(range(1,11))
for num in numbers:
	cube = f'Cube of {num} is {num**3}'
	cubes.append(cube)
for cube in cubes:
	print(cube)