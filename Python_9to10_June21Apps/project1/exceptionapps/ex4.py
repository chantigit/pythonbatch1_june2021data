def work1():
    n1,n2,res=0,0,0
    try:
        n1 = int(input('Enter n1 value:'))
        n2 = int(input('Enter n2 value:'))
        res=n1/n2
    except ValueError:
        print('Invalid input')
    except ZeroDivisionError:
        print('Cannot divide by zero')
    else:
        print('Division is:',res)
    finally:
        del n1, n2, res
        print('--finally--')
work1()