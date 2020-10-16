#version 1 with only if blocks
shot_alien_colour = 'green'
if shot_alien_colour.lower() == 'green':
	print('The Player has earned 5 points')
if shot_alien_colour.lower() != 'green':
	print('The Player has earned 10 points')

#version 2 with else block also...
shotalien_colour = 'green'
if shotalien_colour.lower() == 'green':
	print('The Player has earned 5 points')
else:
	if shotalien_colour.lower() != 'green':
		print('The Player has earned 10 points')