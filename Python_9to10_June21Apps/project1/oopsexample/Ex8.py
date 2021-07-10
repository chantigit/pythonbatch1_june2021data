class P1:
    def task(self):
        print('Hello from P1.task() method')
class P2:
    def task(self):
        print('Hi from P2.task() method')

class C(P2,P1):
    pass

ob=C()
ob.task()