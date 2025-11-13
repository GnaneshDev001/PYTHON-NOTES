import csv,requests,json,mysql.connector
try:
    data=requests.get('https://dummyjson.com/products')
    products=data.json()['products']
    products_data_t=[]
    products_data_d=[]
    for product in products:
        products_data_t.append((
            product['id'],
            product['title'],
            product['price'],
            product['category'],
            product['rating'],
        ))
        products_data_d.append({
            "uid":product['id'],
            "uname":product['title'],
            "price":product['price'],
            "category":product['category'],
            "rating":product['rating'],
        })
#json file:
    fp=open('product.json','w')
    json.dump(products_data_d,fp)
    print("new json file created")
#csv file:
    fp1=open('product.csv','w',newline="")
    obj=csv.writer(fp1)
    obj.writerow(['uid','title','price','category','rating'])
    obj.writerows(products_data_t)
    print("new csv file created")
#mysql new table creation
    dbcon=None
    cursor=None
    dbcon=mysql.connector.connect(host='localhost',
                                username='root',
                                password='root',
                                database='gnana')
    print(dbcon.is_connected())
    cursor=dbcon.cursor()
    sql_st='''
    create table  Products(
                        uid int primary key,
                        uname varchar(64) not null,
                        price float,
                        category varchar(64) not null,
                        rating float );'''
    cursor.execute(sql_st)
    sql_st='''INSERT INTO Products(uid, uname, price, category, rating) VALUES (%s, %s, %s, %s, %s)'''
    
    cursor.executemany(sql_st,products_data_t)
    dbcon.commit()
    print("New MYSQl table created")
except mysql.connector.Error as err:
    print(err)
finally:
    cursor.close()
    dbcon.close()
    fp.close()
    fp1.close()