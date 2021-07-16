def work1():
    try:
        try:
            res = 150 / 0
            print('Division is:', res)
        except ZeroDivisionError:
            print('Cannot divide by zero')
        finally:
            print('END1')
        s1='Hello'
        print(s1[14])
    except IndexError:
        print('Given index is not available')
    finally:
        print('END2')

work1()