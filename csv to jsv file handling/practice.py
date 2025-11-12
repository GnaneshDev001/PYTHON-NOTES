import json,csv
fp=open('user.csv','r')
data=list(csv.DictReader(fp))
fp=open('userr.json','w')
emp=json.dump(data,fp)

