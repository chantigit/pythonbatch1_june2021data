import pymysql
def deleteStudentRow():
    dbcon = pymysql.connect(host='localhost', user='root', password='root', database='pythondb2')
    cursor = dbcon.cursor()
    deleteQuery1 = '''delete from student where id=1'''
    cursor.execute(deleteQuery1)
    dbcon.commit()
    print('Row is deleted')
    
deleteStudentRow()