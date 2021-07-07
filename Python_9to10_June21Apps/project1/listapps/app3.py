#Iterable & Iterator (next() & iter() functions)

#Preparing iterable using list
setA={10,2,30,4,50}
#Preparing iterator
elements=iter(setA)
print(next(elements))  #10
print(next(elements))  #2
print(next(elements))  #30
print(next(elements))  #4
print(next(elements))  #50
print(next(elements))  #