def work1():
    try:
        print(10/0)
    except ZeroDivisionError:
        print('Cannot divide by zero')
    except Exception as e:
        print('Ur exception was caught,i.e: ',e.__class__)
work1()