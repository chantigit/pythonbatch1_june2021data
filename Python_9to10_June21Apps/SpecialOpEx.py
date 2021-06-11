#1.Identity operator  (is,is not)
a=10
b=20
c=10
d=20
print(id(a))  #address of a
print(id(b))  #address of b
print(id(c))  #address of c
print(id(d))  #address of d
print(a is b) #False
print(a is c) #True
print(a is not c) #False
print(a is not b) #True
#2.Membership operator (in,not in)
studentnames=['arun','ajay','varun','senu','depak']
print('ajay' in studentnames)
print('pavan' in studentnames)
print('pavan' not in studentnames)
