from re import findall
print(findall(r'\AThe',r'The moon'))
print(findall(r'\AThe',r'In The moon'))
print(findall(r'\Buni',r'communication'))
print(findall(r'\Buni',r'unidirection'))
print(findall(r'\d',r'abc'))
print(findall(r'\d',r'a11b22c'))
print(findall(r'\D',r'a11b22c'))
print(findall(r'\D',r'555'))