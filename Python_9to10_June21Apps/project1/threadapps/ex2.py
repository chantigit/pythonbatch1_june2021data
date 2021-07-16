#Multithreading in Python
from time import sleep
from threading import Thread
class Job1(Thread):
    def task1(self):
        for i in range(1,6):
            print('Job1.task1() prints i=',i)  #1
            #sleep(1)   #Non-Runnable State
    def run(self) :   #Running State
        self.task1()
class Job2(Thread):
    def task2(self):
        for i in range(6,11):
            print('Job2.task2() prints i=',(i/0))
            #sleep(1)
    def run(self):
        self.task2()
class Job3(Thread):
    def task3(self):
        for i in range(11,16):
            print('Job3.task3() prints i=',i)
            #sleep(1)
    def run(self):
        self.task3()
obj1=Job1()     #New State
obj2=Job2()
obj3=Job3()
obj1.start()    #Runnable State
obj2.start()
obj3.start()
