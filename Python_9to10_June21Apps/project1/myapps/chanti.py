#Variables
a,b,c,d=10,20,300,400
#Functions
def sayhi():
    print('Hi Chanti')
def sayhello():
    print('Hello Chanti')
def saybye():
    print('Bye Chanti')
#Classes
class Addition:
    def __init__(self,x,y):
        self.x,self.y=x,y
    def dosum(self):
        print('Sum is:',(self.x+self.y))
class EvenOrOdd:
    @staticmethod
    def isevenorodd(num):
        if num%2==0:
            print('Your number is even')
        else:
            print('Your number is odd')