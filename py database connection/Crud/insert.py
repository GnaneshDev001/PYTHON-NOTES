import mysql.connector
dbcon=None
cursor=None
try:
    dbcon=mysql.connector.connect(host='localhost',username='root',password='root',database='db4')
    print(dbcon.is_connected())
    cursor=dbcon.cursor()
    sql_st='''
    insert into employees values
    (101,'Gnanesh','gnana@gmail.com','banglore');
    '''
    cursor.execute(sql_st)
    dbcon.commit()
    print("data inserted Successfully")
except mysql.connector.Error as err:
    print(err)
finally:
    cursor.close()
    dbcon.close()