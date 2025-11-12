import json
fp=open('data.json','r')
data=json.load(fp)
print(data)
fp.close()
#write to new file
import json
fp=open('data.json','r')
fp1=open('new.json','w')
data=json.load(fp)
json.dump(data,fp1)
print("new file created")
print(fp1)
#dumps()
import json
emp_str='''
[
    {"eid":101,"name":"gnanesh","gender":"male","age":21},
    {"eid":102,"name":"harish","gender":"male","age":22},
    {"eid":103,"name":"vivek","gender":"male","age":23},
    {"eid":104,"name":"balaji","gender":"male","age":21}
]'''
data=json.dumps(emp_str)
print(type(data))
print(data)