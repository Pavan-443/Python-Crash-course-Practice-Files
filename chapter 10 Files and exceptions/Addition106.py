print('Enter q at any time to exit')
print("\nGive two numbers I will give you sum of both")
num1 = input('Please enter the first number: ')
num2 = input('Please enter the second number: ')
try:
    result = int(num1) + int(num2)
except ValueError:
    print('Please enter a valid Number(s)!')
else:
    print(f"\nsum of given two numbers is: {result}")