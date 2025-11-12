import requests,json,csv,mysql.connector
try:
    fp=open('new.json','w')
    fp1=open('new.csv','w',newline="")
    resp_data=requests.get('https://jsonplaceholder.typicode.com/users')
    data=resp_data.json()
    user_data_t=[]
    user_data_d=[]
    for dat in data:
        user_data_d.append({
        "uid":dat['id'],
        "uname":dat['username'],
        "email":dat['email'],
        "city":dat['address']['city'],
        })
        user_data_t.append((dat['id'],
        dat['username'],
        dat['email'],
        dat['address']['city'],
        ))
    #json file
    data1=json.dump(user_data_t,fp)
    print("new json file created")
    #csv file
    cw=csv.writer(fp1)
    cw.writerow(['id','name','email','city'])
    cw.writerows(user_data_d)
    print('new csv file created')
#mysql connection
    dbcon=None 
    cursor=None
    dbcon=mysql.connector.connect(host='localhost',
                                  user='root',
                                  password='root',
                                  database='db4')
    print(dbcon.is_connected())
    cursor=dbcon.cursor()
    sql_st='insert into users(id,username,email,city) values(%s,%s,%s,%s);'
    cursor.executemany(sql_st,user_data_t)
    dbcon.commit()
    print('New Mysql Table created Successfully') 
except mysql.connector.Error as err:
    print(err)
finally:
    cursor.close()
    dbcon.close()
    fp.close()
    fp1.close()

