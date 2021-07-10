class Task1:
    def job(self,a,b):
        print('Task1.job(): ',(a+b))

class Task2(Task1):
    def job(self,a,b):
        super().job(2,10)
        print('Task2.job(): ',(a**b))

ob=Task2()
ob.job(2,10)  #1.P  2.C  3.P & C  4.None