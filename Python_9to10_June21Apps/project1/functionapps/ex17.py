def showMyData(a):
    print('inside showMydata: before modifiy::a=',a)
    a=a+400
    print('inside showMydata: after modifiy:: a=', a)
def showMyData1(b):
    print('inside showMydata1: before modifiy::b=',b)
    b[0]=100
    b[1]=200
    print('inside showMydata1: after modifiy:: b=', b)  #100,200,30
if __name__=='__main__':
    x=100
    showMyData(x)   #Call by Value
    print('inside main()::x=',x)
    y=[10,20,30]
    showMyData1(y)  #Call by Reference
    print('inside main()::y=', y)
