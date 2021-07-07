listA=[10,20,6,0,3,9,8,7,5,1,252,36]
tupleA=(10,20,6,0,3,9,8,7,5,1,252,36)
setA={10,20,6,0,3,9,8,7,5,1,252,36}
print(listA)
print(tupleA)
print(setA)
'''
#Accessing collection elements using for each loop(element based accessing)
for i in listA:
    print(i)
for i in setA:
    print(i)
'''
#Accessing collection elements using for loop(index based accessing)
for i in range(len(listA)):  #range(12)  =>i = 0 to 11
    print(listA[i])
for i in range(len(setA)):  #range(12)  =>i = 0 to 11
    print(setA[i])