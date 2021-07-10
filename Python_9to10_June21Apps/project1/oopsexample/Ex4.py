class Student:
    #Declaring static variables
    courseName='Python'
    trainerName='Chanti'
    #Declaring instance varibles
    def __init__(self,rollNumber,name,age):
        self.rollNumber=rollNumber
        self.name=name
        self.age=age
    def __str__(self):
        return Student.courseName+','+Student.trainerName+','+str(self.rollNumber)+','+self.name+','+str(self.age)

#Object creation
student1=Student(1,'Ajay',26)
print(student1)
student2=Student(2,'Depak',24)
print(student2)
student3=Student(3,'Vinay',25)
print(student3)