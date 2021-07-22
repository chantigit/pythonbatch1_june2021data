
def readdatafromfile():
    fv=open('info.txt','r')
    mydata=fv.read()
    print(mydata)
    sp=0
    for i in mydata:
        if i==' ':
            sp=sp+1
    print('Spaces=',sp)
    print('Words=', sp+1)
    fv.close()

readdatafromfile()