emp={
    "eid":101,
    "ename":"John",
    "esal":50000
}
print(emp.get('eid'))
print(emp.get('loc'))#if key is not found it returns None 
for key in emp.keys():
    print(key,":",emp.get(keys))