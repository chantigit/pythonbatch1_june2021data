def sum1(a,b,c):
    print(a+b+c)
sum1(10,20,30)
#sum1()            #sum1() missing 3 required positional arguments: 'a', 'b', and 'c'
#sum1(100)        #sum1() missing 2 required positional arguments: 'b' and 'c'
#sum1(100,200)    #sum1() missing 1 required positional argument: 'c'
#DEFAULT PARAMETERS
def sum2(m=10,n=20,o=30):
    print(m+n+o)

sum2()
sum2(100)
sum2(7,8)
sum2(4,5,6)

def work1(a,b=70,c=60):
    print(a,b,c)

work1(7,8,9)
work1(4,5)
work1(7)
#work1()  #work1() missing 1 required positional argument: 'a'

#Rule:
#def work2(a,b,g=100,h,i): #non-default parameter follows default parameter


