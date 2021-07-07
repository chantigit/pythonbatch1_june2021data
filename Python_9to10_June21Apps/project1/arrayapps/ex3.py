import array as ar
#Preparing One Dimensional Array
v1=ar.array('i',[1,2,3])
print(v1)
'''
#Preparing Two Dimensional Array
v2=ar.array('i',[[1,2,3],[11,22,33]])
print(v2)
'''
listA=[ [1,2,3],[4,5,6]  ]
listB=[ [1,2,3],[4,5,6]  ]
print(listA)
print(listB)

listC=[[],[]]
'''
for i in range(2):   #0,1
    for j in range(3): #0,1,2
        listC[i][j]=listA[i][j]+listB[i][j]
'''
print(listC)
#Drawbacks with array: We cannot prepare 2D,3D,MD arrays
#Solution is NumPy
for i in range(2):
    for j in range(3):
        print(listA[i][j])
for i in range(2):
    for j in range(3):
        print(listB[i][j])
for i in range(2):
    for j in range(3):
        print(listA[i][j]+listB[i][j],end=' ')
    print()
