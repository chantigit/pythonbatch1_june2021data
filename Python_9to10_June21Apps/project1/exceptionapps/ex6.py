def divide(a,b):
    try:
        if b!=0:
            c = a / b
            print('Division=',c)
        else:
            raise ZeroDivisionError()
    except ZeroDivisionError:
        print('Cannot divide by zero')

divide(100,2)
divide(0,2)
divide(100,0)