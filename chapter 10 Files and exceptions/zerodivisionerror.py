while True:
    print('This program takes two numbers and then gives their quotient')
    try:
        num1 = float((input('please enter the first number: ')))
        num2 = float((input('please enter the second number: ')))
        result = num1/num2
    except ZeroDivisionError:
        print('\nYou cannot divide a number by zero!\n')
    except ValueError:
        print('\nplease Enter a valid input!\n')
    except Exception:
        print('\nsorry an error has occurred!\n')
    else:
        print(f"Quotient of {num1}/{num2} is {result}")
        break
