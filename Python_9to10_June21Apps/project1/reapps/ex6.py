from re import findall
print(findall(r'[abc]',r'a'))
print(findall(r'[abc]',r'bc'))
print(findall(r'[abc]',r'apple is bat'))
print(findall(r'[abc]',r'zoo'))

print(findall(r'.',r'a'))
print(findall(r'..',r'a'))
print(findall(r'...',r'ab'))
print(findall(r'....',r'abcd'))


print(findall(r'app*e',r'appe'))
print(findall(r'ap*e',r'appe'))
print(findall(r'ma*n',r'mn'))
print(findall(r'ma*n',r'maan'))
print(findall(r'ma+n',r'mn'))
print(findall(r'ma+n',r'man'))
print(findall(r'ma?n',r'mn'))
print(findall(r'ma?n',r'man'))
print(findall(r'ma?n',r'maan'))

print(findall(r'a{2,3}',r'abc'))
print(findall(r'a{2,3}',r'aaabc'))
print(findall(r'a{2,3}',r'aaaaabc'))
print(findall(r'a{2,3}',r'aaaabc'))


print(findall(r'a|b',r'def'))
print(findall(r'a|b',r'arg'))
print(findall(r'a|b',r'apple bat'))


print(findall(r'(a|b|c)yz',r'abc xyz'))
print(findall(r'(a|b|c)yz',r'ayz byz aayz dyz'))