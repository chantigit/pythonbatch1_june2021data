def sayHi():
    return 'Hi'
def sayBye():
    return 'Bye'
def showMyData(a,b,c,d,e,f):
    print(e())
    print(a,b,c,d)
    print(f())

p,q,r,s='Ajay',25,6.9,['singing','cooking','gardening']
#Passing function as argument
showMyData(p,q,r,s,sayHi,sayBye)