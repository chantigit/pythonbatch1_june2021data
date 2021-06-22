def one():        #Outer function
    print('Hi')
    def two():     #Inner function
        print('Hello')
    two()

one()