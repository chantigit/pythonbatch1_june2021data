print('HELLO1')
def wish():
    print('Good morning')
def sayHi():
    print('Hi')
def sayBye():
    print('Bye')
#Called function
def entry():
    print('Entry of main')
    sayHi()
    wish()
    sayBye()
    print('Exit of main')
#Calling function
if __name__ == '__main__':
    entry()
print('HELLO2')