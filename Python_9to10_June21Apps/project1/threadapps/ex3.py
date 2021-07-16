from threading import  Thread
from time import sleep
class Job:
    def task1(self,tn):
        for i in range(1,5):
            print(tn,' prints i=',i)
            sleep(1)

class A(Thread):
    def run(self):
        ob=Job()
        print(self.getName(), ' status before join is:', self.is_alive())
        ob.task1(self.getName())
class B(Thread):
    def run(self):
        ob = Job()
        print(self.getName(), ' status before join is:', self.is_alive())
        ob.task1(self.getName())

t1=A()
t2=B()
t1.setName('Arun')
t2.setName('Ajay')
t1.start()
t1.join() #Holds current thread execution until it complete its work
t2.start()
t2.join() #Holds current thread execution until it complete its work
print(t1.getName(),' status after join is:',t1.is_alive())
print(t2.getName(),' status after join is:',t2.is_alive())