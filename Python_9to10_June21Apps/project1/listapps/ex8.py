#Single List
student=[1,'Ajay',550,'Hyd','Male',['singing','surfing','gardening']]
#Nested List
students=[
    [1,'Ajay',550,'Hyd','Male',['singing','surfing','gardening']],
    [2,'Arun',450,'Chennai','Male',['gardening']],
    [3,'Siri',555,'Pune','Female',['singing','gardening']]
]
for stud in students:
    for r in stud:
        print(r,end=' ')
    print()







#Accessing list elements
print(student[0])
print(student[5])
#Accessing nested-list elements
print(student[5][0])
print(student[5][2])

listA=[1,[2,3],[4,5,6]]
#Access 3
print(listA[1][1])
#Acess 6
print(listA[2][2])

#Accessing elements from nested list using for loop
listB=[[1,2,3],[4,5,6],[7,8,9]]
for i in listB:
    for j in i:
        print(j,end=' ')
    print()