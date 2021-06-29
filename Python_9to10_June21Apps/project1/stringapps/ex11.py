s='One apple cost is 60 rupees'
vc=0
for i in s:
    if i=='a' or i=='e' or i=='i' or i=='o' or i=='u':
        vc=vc+1

print('Vowels=',vc)
