def decor1(fun):
    def inner(a,b,c):
        res=fun(a,b,c)+1
        return res
    return inner

def decor2(dummytotal):
    def inner(l,k,j):
        res=dummytotal(l,k,j)-30
        return res
    return inner

@decor1
@decor2
def total(i1,i2,i3):
    return i1+i2+i3

print(total(100,600,300))