'''
    len(),min(),max(),sum()
	copy(),count(),index(),reverse(),sort()
'''
listA=list()
listA=listA+[10,2,60,90,30,44,2,5,2]
print(len(listA))
print(min(listA))
print(max(listA))
print(sum(listA))
print(listA.count(2))
print(listA.index(90))

listB=listA.copy()
print('After copying: listB=',listB)
listB.sort()
print(listB)
listB.reverse()
print(listB)