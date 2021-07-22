import pymysql
def showStudents():
    dbcon = pymysql.connect(host='localhost', user='root', password='root', database='pythondb2')
    cursor = dbcon.cursor()
    selectQuery = '''select * from student'''
    cursor.execute(selectQuery)
    for i in cursor.fetchall():
        print(i)

    
showStudents()