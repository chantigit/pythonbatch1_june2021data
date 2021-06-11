#Assignment operator
a=10           #1.Single variable assigning
b=c=20         #2.multi variable assigning
d,e,f=30,40,50 #2.multi variable assigning
g=c+e          #3.Storing result
print(g)
#4.swapping
print(b,d)     #20 30
b,d=d,b
print(b,d)     #30 40
#5.Shorthand operation
a+=90
print(a)
a*=5
print(a)
a-=200
print(a)
a/=40
print(a)   #7.5    
