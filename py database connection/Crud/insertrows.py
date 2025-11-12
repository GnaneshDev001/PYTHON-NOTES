import mysql.connector
dbcon=None
cursor=None
try:
    dbcon=mysql.connector.connect(host='localhost',username='root',password='root',database='db4')
    print(dbcon.is_connected())
    cursor=dbcon.cursor()
    sql_st='''
    insert into employees(eid,ename,email,city) values(%s,%s,%s,%s);
    '''
    employees=[(102,'Chandu','chandu@gmail.com','chittor'),
    (103,'Chandu','chandu@gmail.com','chittor'),
    (104,'madhu','madhu@gmail.com','chittor'),
    (105,'mahi','mahi@gmail.com','chittor'),
    (106,'sohi','sohi@gmail.com','chittor'),
    ]
    cursor.executemany(sql_st,employees)
    dbcon.commit()
    print("data inserted Successfully")
except mysql.connector.Error as err:
    print(err)
finally:
    cursor.close()
    dbcon.close()