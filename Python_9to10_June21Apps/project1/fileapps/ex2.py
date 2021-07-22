def readdatafromfile():
    fv=None
    try:
        fv=open('D:\info.txt')
    except FileNotFoundError:
        print('Your file is not available in My HD')
    else:
        mydata = fv.read()
        print(mydata)
    finally:
        if fv !=None:
           fv.close()

readdatafromfile()