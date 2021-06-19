#10.Aliasing the function
def one():
    print('Hi')

#Calling Function
one()
#Printing Function Name: Return id/address of function(<function one at 0x000001B6773BE040>)
print(one)
two=one
print(two)
two()
one()
