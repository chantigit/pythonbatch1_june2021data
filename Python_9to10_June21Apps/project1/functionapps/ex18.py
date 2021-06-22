#find grade of 6 subject marks : A/B/C/D
def grade(a,b,c,d,e,f):          #Outer function
    def total():                #Inner function1
        return (a + b + c + d + e + f)
    def percentage():           #Inner function2
        res = total() / 600 * 100
        return res
    per=percentage()
    if per>70:
        print('A')
    elif per<70 and per>60:
        print('B')
    elif per<60 and per>50:
        print('C')
    else:
        print('D')

grade(77,38,49,66,55,44)