import requests,json,csv
fp=open('new.json','w')
fp1=open('new.csv','w', newline="")
#extract
data=requests.get("https://jsonplaceholder.typicode.com/users")
users=data.json()
#transform
json_data=[]
csv_data=[]
for user in users:
    json_data.append({"id":user['id'],
   "name": user['username'],
   
    "email":user['email'],
    "city":user['address']['city']})
    csv_data.append((user['id'],
    user['username'],
    user['email'],
    user['address']['city']))
#json file load
userr=json.dump(json_data,fp)
#csv file load
cw=csv.writer(fp1)
cw.writerow(['id','username','email','city'])
cw.writerows(csv_data)
