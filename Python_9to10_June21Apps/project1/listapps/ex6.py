#List comprehension
#for i in range(5):    0 to 4
#for i in range(5,11): 5 to 10

listA=[i for i in range(5)]
print(listA)   # 0,1,2,3,4
listB=[i for i in range(5,11)]
print(listB)   # 5 to 10
listC=[i**2 for i in range(5)]
print(listC)
listD=[i%2 for i in range(11)]
print(listD)
listE=["even" if i%2==0 else "odd" for i in range(11)]
print(listE)