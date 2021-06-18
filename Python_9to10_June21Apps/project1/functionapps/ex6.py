num=1000
def one():
    a=10
    global num
    num=num+50
    print('inside one() function:a=',a,',num=',num)
def two():
    b=100
    global num
    num=num+500
    print('inside two() function:b=',b,',num=',num)

one()   #a=10 ,num=1050
two()   #b=100 , num=1550