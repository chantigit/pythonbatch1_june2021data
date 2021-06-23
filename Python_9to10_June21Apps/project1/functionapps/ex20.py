#without recursion
def fact1(num):
    f=1
    for i in range(1,num+1):
        f=f*i                 #1*1    1*2    2*3   6*4   24*5   120*6
    return f
#with recursion
def fact2(num):
    if num==1:
        return 1
    else:
        return num*fact2(num-1)  #6*5*4*3*2*1

def main():
    print(fact1(6))
    print(fact2(6))
if __name__ == '__main__':
    main()