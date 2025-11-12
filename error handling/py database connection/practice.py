import mysql.connector
dbcon=None
cursor=None
try:
    dbcon=mysql.connector.connect(host='localhost',
    user='root',
    password='root',
    database='db5')
    print(dbcon.is_connected())
    cursor=dbcon.cursor()
    sql_st='''
            create table employees(
            uid int,
            uname varchar(32),
            salary int
            );
    '''
    sql_st='insert into employees values(%s,%s,%s)'
    data=[(102,"Madhu",42000.0),(101,"Gnanesh",42000.0)]
    cursor.executemany(sql_st,data)
    dbcon.commit()
    print("new mysql table employees created")
except mysql.connector.Error as err:
    print(err)
finally:
    cursor.close()
    dbcon.close()
