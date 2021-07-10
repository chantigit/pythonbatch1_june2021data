class Calculator:
    def __init__(self,num1,num2):
        print('*****CONSTRUCTOR*****')
        self.num1,self.num2=num1,num2
    def add(self):
        res=self.num1+self.num2
        print('Addition is:',res)
    def sub(self):
        res = self.num1 - self.num2
        print('Substraction is:', res)
    def __str__(self):
        print('*****STR*****')
        return str(self.num1)+','+str(self.num2)
    def __del__(self):
        print('*****DESTRUCTOR*****')
        del self.num1,self.num2

user1=Calculator(10,200)
print(user1)
user1.add()
user1.sub()
