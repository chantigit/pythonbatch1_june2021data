class Addition:
    #Method Overloading
    def sum(self,a,b):
        print(a+b)
    def sum(self,a,b,c):
        print(a+b+c)
    def sum(self,a,b,c,d):
        print(a+b+c+d)

ob=Addition()
#ob.sum(1,2)
#ob.sum(1,2,3)
ob.sum(1,2,3,4)