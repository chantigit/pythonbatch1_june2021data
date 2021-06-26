def showNumbers():
    yield 1
    yield 2
    yield 3

value=showNumbers()
print(next(value))  #1
print(next(value))  #2
print(next(value))  #3
#print(next(value))  #1 :: ERROR->StopIteration