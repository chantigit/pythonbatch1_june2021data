s1='Python by chanti'
print(s1.startswith('Py'))
print(s1.startswith('by'))
print(s1.endswith('Py'))
print(s1.endswith('nti'))
print(s1.find('by'))    #index of b i.e 7
print(s1.find('n'))     #index of n i.e 5 from left
print(s1.rfind('n'))    #index of n i.e 13 from right
print(s1.find('B'))     #index of B i.e -1 (not found)