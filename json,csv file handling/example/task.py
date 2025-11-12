#read emp.json file and print 
#no of male and female employees

# import json 
# fp=open('employee.json','r')
# emp_data=json.load(fp)
# male_count=0
# female_count=0
# for emp in emp_data:
#     if emp['gender']=="Male":
#         male_count=male_count+1
#     elif emp['gender']=="Female":
#         female_count=female_count+1
# print("female Employees:",female_count)
# print("male Employees:",male_count)

# fp.close()

import json 
fp=open('employee.json','r')
emp_data=json.load(fp)
for emp in emp_data:
    if emp['gender']=="Male":
        print("male Employees:",emp)
    
fp.close()