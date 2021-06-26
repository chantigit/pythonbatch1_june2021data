def evenGenerator(num):
    s=0
    for i in range(1,num+1):  #1->5
        s=s+2
        yield s

value=evenGenerator(5)
print(next(value)) #2
print(next(value)) #4
print(next(value)) #6
print(next(value)) #8
print(next(value)) #10
