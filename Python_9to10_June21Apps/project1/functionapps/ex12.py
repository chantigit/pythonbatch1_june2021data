#Arbitary argument / Variable length arguments
def totalItems(*a):
    s=0
    for i in a:
        s=s+i
    print('Total bill is:',s)

totalItems(10)
totalItems(10, 20)
totalItems(10, 20, 30, 40)
totalItems(10, 20, 30, 40, 50, 60, 70, 80, 90)
#can we pass in a different type some are int and some of then double or float
def showMyData(*details):
    print('Your details are:',details)

showMyData('Arun')
showMyData('Arun',25)
showMyData('Arun',25,9.8)
'''
def myFun(*a):
    print(a)
    print(type(a)) 

myFun(10)
myFun(10, 20)
myFun(10, 20, 30, 40)
myFun(10, 20, 30, 40, 50, 60, 70, 80, 90)
'''
