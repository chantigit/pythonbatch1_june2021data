s='java has 2 parts i.e core java and adv java'
print(s.replace('java','python'))
print(s)
print(s.split(' '))
print('@'.join(s))
print('$'.join(s))
a,b=10,20
s='{} + {} = {}'.format(a,b,(a+b))
print(s)

s="Google"
print(s.index('G'))
print(s.index('g'))
print(s.index('o'))
print(s.rindex('o'))
#print(s.index('L'))   #ValueError: substring not found
print(s.count('o'))