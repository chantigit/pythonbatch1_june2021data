#Dev1 code
class Task1:
    def sum(self,a,b):
        print('C1:Addition of {} and {} is :{} '.format(a,b,(a+b)))
#Dev2 code
class Task2(Task1):
    def mul(self, a, b):
        print('C2:Multiplication of {} and {} is :{} '.format(a, b, (a * b)))
class Task3(Task2):
    def div(self, a, b):
        print('C3:Division of {} and {} is :{} '.format(a, b, (a / b)))
class Task4(Task2):
    def mod(self, a, b):
        print('C4:Mod of {} and {} is :{} '.format(a, b, (a % b)))

class Task5(Task3,Task4):
    def sub(self,a,b):
        print('C5:Sub of {} and {} is :{} '.format(a, b, (a - b)))
print('-----accessing ob1 members-----')
ob1=Task1()
ob1.sum(55,66)
print('-----accessing ob2 members-----')
ob2=Task2()
ob2.sum(565,266)
ob2.mul(10,2)
print('-----accessing ob3 members-----')
ob3=Task3()
ob3.sum(565,266)
ob3.mul(10,2)
ob3.div(45,9)
print('-----accessing ob4 members-----')
ob4=Task4()
ob4.sum(565,266)
ob4.mul(10,2)
ob4.mod(45,6)
print('-----accessing ob5 members-----')
ob5=Task5()
ob5.sub(450,63)
ob5.sum(565,266)
ob5.mul(10,2)
ob5.mod(45,6)
ob5.div(95,3)