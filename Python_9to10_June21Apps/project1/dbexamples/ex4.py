import pymysql
def updateStudentRow():
    dbcon = pymysql.connect(host='localhost', user='root', password='root', database='pythondb2')
    cursor = dbcon.cursor()
    updateQuery1 = '''update student set name='vijay' where id=1'''
    cursor.execute(updateQuery1)
    dbcon.commit()
    print('Row is updated')
    
updateStudentRow()