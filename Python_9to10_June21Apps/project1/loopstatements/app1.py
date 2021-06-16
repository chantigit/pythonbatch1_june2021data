#Print 1,2,3,4,5
n=5
for i in range(1,n+1):
    print(i)
#Print sum of n natural numbers : 1+2+3+4+5
n=5
s=0
for i in range(1,n+1):
    s=s+i   #s=0+1 =1  ,  s=1+2=3   ,  s=3+3=6  , s=6+4=10 , s=10+5=15
print('s=',s)
#Print factorial of a number : 1*2*3*4*5
s,n=1,5
for i in range(1,n+1):
    s=s*i  #s=1*1 =1 ,   s=1*2=2  , s=2*3=6 ,  s=6*4=24 , s=24*5 = 120
print('s=',s)
'''
    5 * 1 = 5
    5 * 2 =10
    ..
    5 * 10=50
'''
n=5
for i in range(1,11):
    print(n,'*',i,'=',(n*i))

#Print factors of a number
#n=8  : 1,2,4
#n=10 : 1,2,5
#n=28 : 1,2,4,7,14
n=28
for i in range(1,n//2+1):
    if n%i==0:
        print(i)
















