#A function can used as return statement to another function
#Example1:
def square(a):      #function1
    return a * a
def cube(num):     #function 2
    return square(num)*num
print(cube(10))

#Example2:
def wish1():
    return 'Hello'
def sayHi():
    return wish1()

print(sayHi())



