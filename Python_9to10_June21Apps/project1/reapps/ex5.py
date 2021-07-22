from re import findall
print(findall(r'^a...c$',r'abc'))
print(findall(r'^a...c$',r'abbbc'))
print(findall(r'^a...c$',r'acdec'))
print(findall(r'^a...c$',r'ahhhhhhc'))
print(findall(r'^a.c$',r'abc'))

