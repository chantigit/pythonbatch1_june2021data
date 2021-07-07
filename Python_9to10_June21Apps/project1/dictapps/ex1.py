#1.Creating empty dict
a={}
b=dict()
#2.Creating dict with key,value
c={'id':21,'name':'Ajay','height':5.6,'age':21,'name':'Arun'}
print(type(a),type(b),type(c))
print(c)
#3.Accessing dict values based on keys
print(c['id'])
print(c['name'])
print(c['age'])
print(c['height'])
#4.Updating the dict
c['height']=6.9
c['age']=25
print(c)
#5.Deleting a pair from dict
del c['age']
print(c)
#6.Adding new pairs to exisitng dict
c['city']='Hyd'
c['phone']=9849098490
print(c)

print(c.get('city'))
c.pop('phone')
print(c)
c.clear()
print(c)