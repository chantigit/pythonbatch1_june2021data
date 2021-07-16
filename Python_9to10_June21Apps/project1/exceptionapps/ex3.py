def work1():
    try:
        s1='Hello'
        print(s1[10])
    except IndexError:
        print('Given index is not available')
    else:
        print('--ELSE--')
    finally:
        print('END2')

work1()