#tests for equality and inequality
name = 'Pavan'
print(name == 'Pavan')
print(name != 'pavan')
print(name == 'pavan')
print(name != 'Pavan')
print('\n')

car = 'BMW'
print(car.lower() == 'bmw')
print(car.lower() != 'bmw')
print('\n')

age = 17
print(age == 17)
print(age == 12)
print(age != 14)
print(age != 17)
print(age > 12)
print(age > 19)
print(age < 20)
print(age < 14)
print(age >= 17)
print(age >= 20)
print(age <= 20)
print(age <= 12)
print('\n')

number = 20
age = 15
print(number == 20 and age == 15)
print(number == 20 and age == 20)
print(number == 20 or age == 20)
print(number ==1 or age == 1)
print('\n')

friends = ['jayakar', 'varshith', 'advaith']
print('advaith' in friends)
print('Advaith' in friends)
print('\n')

print('rudheer' not in friends)
print('advaith' not in friends)
