#use of format specifiers(%d,%f,%s)
a,b,c=10,6.9,'Apple'
print('a value=',a)
print('a value= %d'%a)
print('b value= %f,c value is= %s'%(b,c))
n1,n2=100,200
print('%d + %d = %d'%(n1,n2,(n1+n2)))
#use format() function
age,name,height=21,'Arun',6.8
print('AGE= ',age)
print('NAME=',name, 'HEIGHT=',height)
print('AGE= {}'.format(age))
print('NAME={} ,HEIGHT={} '.format(name,age))
print('{} + {} = {}'.format(n1,n2,(n1+n2)))
print('{1} + {0} = {2}'.format(n1,n2,(n1+n2)))



#Use of sep argument  & Use of end argument
'''
a,b,c,d=1,2,3,4
print(a,b,c,d,sep=',')
print(a,b,c,d,sep='@')
print(a,b,c,d,sep='\n')

print('Apple',end='')
print('is',end=' ')
print('a Fruit',end=' ')

a,b,c,d=1,2,3,4
print(a,b,c,sep=',',end=' ')
print(d)

'''