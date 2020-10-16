person1_info = {'first':'mahesh', 'last':'babu', 'age':14, 'city':'markapur'}
person2_info = {'first':'pavan', 'last':'teja', 'age':16, 'city':'kalikiri'}
person3_info = {'first':'paul', 'last':'jayakar', 'age':17, 'city':'tirupati'}
persons = [person1_info,person2_info,person3_info]
for person in persons:
	person['name'] = person['first'].title() + person['last'].title()
	person['location'] = person['city'].title()
	del person['first']
	del person['last']
	del person['city']
	print('\n')
	for key , value in person.items():
		if key == 'name':
			print(f"Persons name is {person['name']}")

	for key , value in person.items():
		if key != 'name':
			print(f"Person's {key} is {value}")