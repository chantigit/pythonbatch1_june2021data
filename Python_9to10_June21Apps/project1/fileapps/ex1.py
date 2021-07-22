def createfileandwrite():
    fv=open('D:\info.txt','w')
    fv.write('HELLO\n')
    fv.write('CHANTI')
    print('---File was created---')
    fv.close()

#createfileandwrite()
def readdatafromfile():
    fv=open('D:\info.txt','r')
    mydata=fv.read()
    print(mydata)
    fv.close()

#readdatafromfile()

def appenddataintofile():
    fv = open('D:\info.txt', 'a')
    fv.write('HOW ARE YOU ?')
    fv.close()

#appenddataintofile()