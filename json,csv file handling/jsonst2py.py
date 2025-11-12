import json
emp_str='''
[
   {"eid":101,"name":"gnanesh","avail":true,"grade":null},
    {"eid":102,"name":"chandu","avail":true,"grade":null},
    {"eid":103,"name":"madhu","avail":true,"grade":null},
    {"eid":104,"name":"balaji","avail":true,"grade":null},
    {"eid":105,"name":"guru","avail":true,"grade":null}
]'''
# fp=open('all.json','w')
# employees=json.loads(emp_str)
# data=json.dump("employees.json",fp)
# print(type(employees))
# print(employees)
data=json.dumps(emp_str)
print(data)
print(type(emp_str))
