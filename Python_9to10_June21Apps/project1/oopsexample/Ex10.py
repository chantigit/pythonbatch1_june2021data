class Addition:
    #Method Overloading is supported by Arbitary Parameters
    def sum(self,*a):
        s=0
        for i in a:
            s=s+i
        print(s)

ob=Addition()
ob.sum(1,2)
ob.sum(1,2,3)
ob.sum(1,2,3,4)
ob.sum(1,2,3,4,5,6,7,8,9,100)