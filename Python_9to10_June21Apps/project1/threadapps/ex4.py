from threading import Thread,Lock
from time import sleep
class BMS:
    totalTickets=10
    def getTickets(self,name,requiredTickets):
        print(BMS.totalTickets,' tickets are available to ',name)
        if requiredTickets>BMS.totalTickets:
            print(requiredTickets,' tickets are not available')
        else:
            for i in range(1,requiredTickets+1):
                print(i,' ticket is issued to ',name)
                BMS.totalTickets=BMS.totalTickets-1
                sleep(1)
lock=Lock()
class A(Thread):
    def run(self):
        ob=BMS()
        lock.acquire()
        ob.getTickets(self.getName(),5)
        lock.release()
class B(Thread):
    def run(self):
        ob = BMS()
        lock.acquire()
        ob.getTickets(self.getName(), 9)
        lock.release()
t1=A()
t2=B()
t1.setName('Arun')
t2.setName('Ajay')
t1.start()
t2.start()
