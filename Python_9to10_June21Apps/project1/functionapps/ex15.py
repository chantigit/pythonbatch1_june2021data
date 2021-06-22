#Python follows top-to-bottom approach

def sayHi():     #called function1
    print('Hi')
def main():
    sayHi()    #calling function1
    sayBye()   #calling function2
if __name__ == '__main__':
    main()
def sayBye():   #called function2
    print('Bye')