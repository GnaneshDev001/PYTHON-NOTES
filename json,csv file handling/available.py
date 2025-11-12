#read json file and print names of available employees

import json
fp=open('data.json.',"r")
employees=json.load(fp)
print(employees)
print(type(employees))
for emp in employees:
    if emp['avail']==True:
        print(emp['name'])

fp.close()