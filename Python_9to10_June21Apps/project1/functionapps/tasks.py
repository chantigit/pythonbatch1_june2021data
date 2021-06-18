#Task2: Power of a number
def power(a,b):
    res=a**b
    print(res)
#Task3: Biggest of 4 numbers
def largestNumber(n1,n2,n3,n4):
    if n1>n2 and n1>n3 and n1>n4:
        print(n1,' is big')
#Task4: Find factorial of a number
def fact(n):
    f=1
    for i in range(1,n+1):
        f=f*i
    print(f)
#Task5: Print reverse of a number
def reverse(n):
    rev=0
    while n>0:
        rem=n%10
        rev=(rev*10)+rem
        n=n//10
    print(rev)

#Calling Functions
power(2,10)  #1024
largestNumber(100,10,20,30) #100
fact(5) #120
reverse(123)