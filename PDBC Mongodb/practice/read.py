import pymongo
from pymongo import MongoClient
client=None;
try:
    client=MongoClient('mongodb://localhost:27017/')
    db=client['db5']
    user_data=db['users']
    data=user_data.find()
    users=list(data)
    for user in users:
        print(user['id'],user['name'])
except:
    print("unable to print")
finally:
    client.close()