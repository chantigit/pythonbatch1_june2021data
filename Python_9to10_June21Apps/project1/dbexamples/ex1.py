import pymysql
def createStudentTable():
    dbcon = pymysql.connect(host='localhost', user='root', password='root', database='pythondb2')
    cursor = dbcon.cursor()
    createQuery = 'create table student(id int primary key,name varchar(20) not null,age int not null);'
    cursor.execute(createQuery)
    print('Table is created')

createStudentTable()