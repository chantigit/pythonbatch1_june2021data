#remove(ele),	pop(index),	clear(),	del keyword
listA=[10,50,60,30,20]
listA.remove(50)
print('After remove:',listA)  #10-0 60-1 30-2 20-3
listA.pop(0)
print('After pop:',listA)
del listA[0]
print('After del:',listA)
listA.clear()
print('After clear:',listA)