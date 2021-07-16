#Single thread in Python
from time import sleep
class Job1:
    def task1(self):
        for i in range(1,6):
            print('Job1.task1() prints i=',(i/0))
            sleep(1)
class Job2:
    def task2(self):
        for i in range(6,11):
            print('Job2.task2() prints i=',i)
            sleep(1)
class Job3:
    def task3(self):
        for i in range(11,16):
            print('Job3.task3() prints i=',i)
            sleep(1)
obj1=Job1()
obj2=Job2()
obj3=Job3()
obj1.task1()
obj2.task2()
obj3.task3()
