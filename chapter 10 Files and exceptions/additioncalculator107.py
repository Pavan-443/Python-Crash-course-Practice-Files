print('Enter q at any time to exit')
while True:
    print("\nGive two numbers I will give you sum of both")
    num1 = input('Please enter the first number: ')
    if num1.lower() == 'q':
        break
    num2 = input('Please enter the second number: ')
    if num2.lower() == 'q':
        break
    try:
        result = int(num1) + int(num2)
    except ValueError:
        print('Please enter a valid Number(s)!')
    else:
        print(f"\nsum of given two numbers is: {result}")
