import json,pymongo,csv,mysql.connector,requests
resp_data=requests.get('https://dummyjson.com/products')
product_data=resp_data.json()
products=product_data['products']

print(len(products))
try:
    json_data=[]
    for product in products:
        json_data.append({"id":product["id"],
                            "name":product["title"],
                            "price":product['price'],
                            "category":product['category'],
                            "rating":product['rating'],})
    #json file 
    fp=open("product.json",'w')
    json.dump(json_data,fp)
    print("new json file created")
    #mongodb:
    client=pymongo.MongoClient('mongodb://localhost:27017/')
    db=client['db4']
    product_col=db['products']
    product_col.insert_many(json_data)
    print("product document inserted successfully")
    #csv file
    csv_data=[]
    for product in products:
        csv_data.append((product["id"],
                            product["title"],
                            product['price'],
                            product['category'],
                            product['rating'],))
    fp1=open("product.csv",'w',newline="")
    cw=csv.writer(fp1)
    cw.writerow(["id","name","price","category","rating"])
    cw.writerows(csv_data)
    #mysql 
    dbcon=None
    cursor=None
    dbcon=mysql.connector.connect(host='localhost',
                                username='root',
                                password='root',
                                database='db4')
    print(dbcon.is_connected())
    cursor=dbcon.cursor()
    sql_st='''
    create table  products(
                        uid int primary key,
                        uname varchar(64) not null,
                        price float,
                        category varchar(64) not null,
                        rating float );'''
    cursor.execute(sql_st)
    sql_st='''INSERT INTO Products(uid, uname, price, category, rating) VALUES (%s, %s, %s, %s, %s)'''
    
    cursor.executemany(sql_st,csv_data)
    dbcon.commit()
    print("New MYSQl table created")
except mysql.connector.Error as err:
    print(err)
finally:
    fp.close()
    fp1.close()
    dbcon.close()
    cursor.close()
