import json,csv,requests,pymongo,mysql.connector
from pymongo import MongoClient
resp_data=requests.get("https://dummyjson.com/products")
data=resp_data.json()
products=data ['products']

#Extraction
product_json=[]
for product in products:
    product_json.append({
                        "pid":product["id"],
                        "name":product["title"],
                        "price":product["price"],
                        "category":product["category"],
                        "rating":product['rating']})
#json file
fp=open("product.json",'w')
json.dump(product_json,fp)
print("json file is created")
#mongodb collection
try:
    client=None;
    client=MongoClient('mongodb://localhost:27017/')
    db=client['db5']
    product_col=db['products']
    product_col.insert_many(product_json)
    print("Mongodb collection created")
except:
    pass
finally:
   fp.close()
#csv file
product_csv=[]
for product in products:
    product_csv.append((
                        product["id"],
                        product["title"],
                        product["price"],
                        product["category"],
                        product['rating']))

fp1=open("product.csv",'w',newline="")
cw=csv.writer(fp1)
cw.writerow(["id","name","price","category","rating"])
cw.writerows(product_csv)
print('new csv file Created')
#mysql
try:
    cursor=None;
    dbcon=None;
    dbcon=mysql.connector.connect(host='localhost',username='root',password='root',database='gnanesh')
    print(dbcon.is_connected())
    cursor=dbcon.cursor()
    sql_st='''create table products(
    id int primary key,
    name varchar(64) not null,
    price float,
    category varchar(32) not null,
    rating float);'''
    cursor.execute(sql_st)
    sql_st='''insert into products(id,name,price,category,rating)values(%s,%s,%s,%s,%s)'''
    cursor.executemany(sql_st,product_csv)
    dbcon.commit()
    print("new mysql table is created")
except mysql.connector.Error as err:
    print(err)
finally:
    fp1.close()
    cursor.close()
    dbcon.close()