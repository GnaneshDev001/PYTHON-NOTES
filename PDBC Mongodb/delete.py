import pymongo
from pymongo import MongoClient
client=None;
try:
    client=MongoClient('mongodb://localhost:27017/')
    db=client['db4']
    user_col=db['users']
    user_data=user_col.find()
    user_col.delete_many({"gender":"Male"})
    print("all male users deleted sucsessfully")
    
except:
    print("unable to print")
finally:
    pass