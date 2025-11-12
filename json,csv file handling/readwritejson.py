#read json file and write to another json file
import json
fp=open('data.json','r')
fp1=open('em.json','w')
employees=json.load(fp)
json.dump(employees,fp1)
print("new file created")
fp.close()
fp1.close()
