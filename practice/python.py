#normal readwrite file:
fp=open('data.txt','r')
data=fp.read()
fp1=open('wish.txt','w')
fp1.write(data)
fp.close()
fp1.close()
#json file read
import json
fp=open('emp.json','r')
data=json.load(fp)
print(data)
fp1=open('empp.json','w')
emp=json.dump(data,fp1)
#loads and jumps
import json
emp_str='''
[
   {"eid":101,"name":"gnanesh","avail":true,"grade":null},
    {"eid":102,"name":"chandu","avail":true,"grade":null},
    {"eid":103,"name":"madhu","avail":true,"grade":null},
    {"eid":104,"name":"balaji","avail":true,"grade":null},
    {"eid":105,"name":"guru","avail":true,"grade":null}
]'''
fp=open('all.json','w')
data=json.loads(emp_str)
json.dump(data,fp)
print("new file created")
fp.close()
#csv readwrite
import csv
fp=open('read.csv','r')
data=csv.reader(fp)
fp=open('write.csv','w')
data1=csv.writer(fp)
for row in data:
    data1.writerow(row)
#write csv file:
import csv
fp=open('wish.csv','w',newline="")
cw=csv.writer(fp)
cw.writerow(['id','name','sal','loc'])
data=[
    (11,'gnana',23000,'banglore'),
    (13,'mahi',28000,'banglore')
]
cw.writerows(data)
fp.close()
#print all users using rest apis url
import requests,json
resp=requests.get("https://jsonplaceholder.typicode.com/users")
data=resp.json()
for user in data:
    print(user['username'],user['address'])
fp=open('write.json','w')
users=json.dump(user,fp)
fp1=open('read.csv','r')
data=list(csv.DictReader(fp1))
fp2=open('writes.json','w')
json.dump(data,fp2)

#ETL operation:
import csv,json,requests
fp1=open('new.json','w')
fp=open('new.csv','w',newline="")
resp=requests.get("https://jsonplaceholder.typicode.com/users")
data=resp.json()
print(type(data))
#transform in json file&csv file
json_data=[]
csv_dataa=[]
for dat in data:
    json_data.append({
        "uid":dat['id'],
        "uname":dat['username'],
        "city":dat['address']['city'],
        "email":dat['email']
    })
    csv_dataa.append([
        dat['id'],dat['username'],dat['address']['city'],dat['email']
    ])
#load
emp=json.dump(json_data,fp1)
cw=csv.writer(fp)
cw.writerow(['id','username','city','email'])
cw.writerows(csv_dataa)
#json to csv
import json,csv
fp=open('emp.json','r')
data=json.load(fp)
print(data)
fp=open('gnana.csv','w')
cww=csv.writer(fp)
cww.writerow(['id','name','salary'])
csv_datta=[]
for dat in data:
    csv_datta.append({
        "id":dat['eid'],
        "name":dat['ename'],
        "salary":dat['salary'],
    })
cww.writerows(csv_datta)
