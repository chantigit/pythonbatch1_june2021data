class Demo1:
    a=10
    _b=100
    __c=1000
    def sayHi(self):
        print('Hi')
    def _sayHello(self):
        print('Hello')
    def __sayBye(self):
        print('Bye')

class Demo2(Demo1):
    def accessingMembersInDemo2(self):
        print('---INSIDE DEMO2---')
        print(Demo1.a,Demo1._b)
        ob=Demo1()
        ob.sayHi()
        ob._sayHello()
class Demo3:
    def accessingMembersInDemo3(self):
        print('---INSIDE DEMO3---')
        print(Demo1.a)
        ob = Demo1()
        ob.sayHi()

ob=Demo2()
ob.accessingMembersInDemo2()
ob1=Demo3()
ob1.accessingMembersInDemo3()

