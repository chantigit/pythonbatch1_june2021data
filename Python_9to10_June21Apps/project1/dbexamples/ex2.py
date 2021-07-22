import pymysql
def saveStudentRow():
    dbcon = pymysql.connect(host='localhost', user='root', password='root', database='pythondb2')
    cursor = dbcon.cursor()
    inserQuery1 = '''insert into student values(1,'Ajay',21)'''
    inserQuery2 = '''insert into student values(2,'Depak',25)'''
    cursor.execute(inserQuery1)
    cursor.execute(inserQuery2)
    dbcon.commit()
    print('Rows are inserted')
    
saveStudentRow()