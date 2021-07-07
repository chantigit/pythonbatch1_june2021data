#1.Class Preparation
class Calculator:
    #2.Data initialization
    def __init__(self,num1,num2):
        self.num1=num1
        self.num2=num2
    #3.Methods
    def add(self):
        res=self.num1+self.num2
        print('Addition is:',res)
    def sub(self):
        res = self.num1 - self.num2
        print('Substraction is:', res)
    def mul(self):
        res = self.num1 * self.num2
        print('Multiplication is:', res)
#4.Object preparation
user1=Calculator(10,200)
#5.Calling methods
user1.add()
user1.sub()
user1.mul()
#4.Object preparation
user2=Calculator(400,60)
#5.Calling methods
user2.add()
user2.sub()
user2.mul()