import array as ar
v1=ar.array('i',[10,20])  #0-10  1-20
#Insert elements into array
v1.append(30)  #2-30
v1.append(40)  #3-40
v1.insert(1,100) #10 100 20 30 40
print(v1)
#Updating elements
v1[3]=300
print(v1)
#Deleting element
del v1[0]
v1.pop(0)
v1.remove(40)
print(v1)
#searching element
print(v1.index(20))
print(v1.index(300))
#Accessing
print(v1[-1])
print(v1[1])