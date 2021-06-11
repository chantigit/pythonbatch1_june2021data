#Logical operators (and  , or , not )
'''
    C1   C2   C1 and C2    C1 or C2    not C1
    
    T    T     T           T           F  
    T    F     F           T           F
    F    T     F           T           T
    F    F     F           F           T
'''
a,b,c=True,False,True
print(a and b)
print(a and c)
print(b and c)

print(a or b)
print(a or c)
print(b or c)

print(a and b or not c)   #False

print(a and b and c)  #False
print(a or b or c)    #True
