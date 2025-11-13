import pymongo
from pymongo import MongoClient
client=None;
try:
    client=MongoClient('mongodb://localhost:27017/')
    db=client['db4']
    user_col=db['users']
    # user_col.insert_one({"uid":101,"uname":"gnanesh"}) insert one row
    users=([{"id":1,"first_name":"Lorri","gender":"Female"},{"id":2,"first_name":"Rusty","gender":"Male"},{"id":3,"first_name":"Rafaellle","gender":"Male"},
    {"id":4,"first_name":"Myrle","gender":"Female"},
    {"id":5,"first_name":"Justinian","gender":"Male"},
    {"id":6,"first_name":"Vinny","gender":"Male"}, 
    {"id":7,"first_name":"Gussi","gender":"Agender"},
    {"id":8,"first_name":"Donaugh","gender":"Male"},
    {"id":9,"first_name":"Blinnie","gender":"Genderqueer"},
    {"id":10,"first_name":"Corbet","gender":"Male"},
    {"id":11,"first_name":"Kissee","gender":"Female"},
    {"id":12,"first_name":"Camila","gender":"Female"},
    {"id":13,"first_name":"Kahlil","gender":"Male"},
    {"id":14,"first_name":"Whitaker","gender":"Male"},
    {"id":15,"first_name":"Bronson","gender":"Male"},
    {"id":16,"first_name":"Daria","gender":"Agender"},
    {"id":17,"first_name":"Rollin","gender":"Male"},
    {"id":18,"first_name":"Carolyn","gender":"Female"},
    {"id":19,"first_name":"Adan","gender":"Male"},
    {"id":20,"first_name":"Iorgo","gender":"Male"},
    {"id":21,"first_name":"Free","gender":"Male"},
    {"id":22,"first_name":"Miranda","gender":"Female"},
    {"id":23,"first_name":"Jard","gender":"Male"},
    {"id":24,"first_name":"Ludovika","gender":"Bigender"},
    {"id":25,"first_name":"Orbadiah","gender":"Male"},
    {"id":26,"first_name":"Jedidiah","gender":"Male"},
    {"id":27,"first_name":"Randie","gender":"Female"},
    {"id":28,"first_name":"Stanwood","gender":"Non-binary"},
    {"id":29,"first_name":"Westbrook","gender":"Male"},
    {"id":30,"first_name":"Charline","gender":"Female"},
    {"id":31,"first_name":"Falito","gender":"Male"},
    {"id":32,"first_name":"Terry","gender":"Female"},
    {"id":33,"first_name":"Cacilie","gender":"Female"},
    {"id":34,"first_name":"Gordan","gender":"Male"},
    {"id":35,"first_name":"Fairleigh","gender":"Male"},
    {"id":36,"first_name":"Diandra","gender":"Bigender"},
    {"id":37,"first_name":"Davey","gender":"Non-binary"},
    {"id":38,"first_name":"Rodrick","gender":"Male"},
    {"id":39,"first_name":"Page","gender":"Female"},
    {"id":40,"first_name":"Arnaldo","gender":"Male"},
    {"id":41,"first_name":"Fulton","gender":"Male"},
    {"id":42,"first_name":"Timi","gender":"Female"},
    {"id":43,"first_name":"Addy","gender":"Male"},  
    {"id":44,"first_name":"Kerri","gender":"Female"},
    {"id":45,"first_name":"Elfrida","gender":"Female"},
    {"id":46,"first_name":"Gerta","gender":"Female"},
    {"id":47,"first_name":"Ricardo","gender":"Male"},
    {"id":48,"first_name":"Geralda","gender":"Polygender"},
    {"id":49,"first_name":"Beatrice","gender":"Female"},
    {"id":50,"first_name":"Augusto","gender":"Male"}])

    print("Document inserted successfully")
    user_col.insert_many(users)
    
except:
    print("unable to print")
finally:
    client.close()