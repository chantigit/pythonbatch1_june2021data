def work1():
    try:
        num1 = int(input('Enter number1:'))
        num2 = int(input('Enter number2:'))
        res = num1 / num2
        print('Division is:', res)
    except ZeroDivisionError:
        print('Cannot divide by zero')
    except ValueError:
        print('Invalid input')
    finally:
        print('END')

work1()