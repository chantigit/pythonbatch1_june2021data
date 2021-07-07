#Called Function
def printElements(items):
    ele=iter(items)
    while True:
        try:
            data=next(ele)
            print(data)
        except StopIteration:
            break
#Calling Function
printElements([80,60,30])
printElements({800,600,300})
printElements((80,60,30))