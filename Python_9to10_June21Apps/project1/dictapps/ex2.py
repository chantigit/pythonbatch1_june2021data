student={'id':501,'Name':'Ajay','age':21}
print(student.keys())
print(student.values())
student.update({'age':22})
print(student.items())

for k in student:
    print(k,'--->',student.get(k))