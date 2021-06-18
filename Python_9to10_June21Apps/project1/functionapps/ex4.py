'''
    1.With parameters 	& With return value
	2.With parameters 	& With out return value
	3.With out parameters 	& With return value
	4.With out parameters 	& With out return value
'''
#PS: Addition of 2 numbers
#Called Functions
def addition1(n1,n2):
    result=n1+n2
    return result
def addition2(n1,n2):
    result = n1 + n2
    print(result)
def addition3():
    n1,n2=3,33
    result=n1+n2
    return result
def addition4():
    n1,n2=4,44
    result=n1+n2
    print(result)
#Calling Functions
r1=addition1(1,11)
print(r1)
addition2(2,22)
r2=addition3()
print(r2)
addition4()