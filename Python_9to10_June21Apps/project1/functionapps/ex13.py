#15.Lambda function  / Anonymous(Without name) function
'''syntax:
variable=labmda  parameters:returnedvalue
ex1:addition of 2 numbers
'''
v1=lambda  n1,n2:n1+n2
r1=v1(10,20)
print(r1)
#ex2:average of 3 numbers
v2=lambda a,b,c: (a+b+c)/3
r2=v2(2,3,5)
print(r2)
#ex3:cube of a number
v3=lambda n:n**3
print(v3(5))
#ex4:power of a number
v4=lambda a,b:a**b
print(v4(2,10))
#ex5:biggest of 2 numbers
big=lambda a,b:a if a>b else b
print(big(10,50))
