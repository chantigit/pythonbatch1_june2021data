#PS1: Addition of 2 numbers using Instance methods (4 Steps of code)
class Addition:
    #Preparing constructor
    def __init__(self,n1,n2):
        self.n1=n1
        self.n2=n2
    #Preparing Instance method
    def doSum(self):
        res=self.n1+self.n2
        print('Sum is:',res)

#Creating object
obj1=Addition(10,20)
#Calling method
obj1.doSum()