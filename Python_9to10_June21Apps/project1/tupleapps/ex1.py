a=(100,99,88,55,44,234,2,1,2,3,1.1,2.2,False,1,2,3,66,22,44,'Apple',6+4j)
b=tuple()
c=1,2,3
print(type(a),type(b),type(c))
print(a)
print(a[0]) #100
print(a[-1]) #6+4j
print(a[-2]) #Apple
#wrtiting new value into a[0]
#a[0]=1000
#TypeError: 'tuple' object does not support item assignment
#del a[1]
#TypeError: 'tuple' object doesn't support item deletion

#tuple functions
print(a.count(2))
print(a.index(22))
print(len(a))