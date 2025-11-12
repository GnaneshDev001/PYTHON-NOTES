# #task1 invoke rest apis and print all users.
# import requests
# resp_data=requests.get('https://jsonplaceholder.typicode.com/users')
# print(type(resp_data))
# users=resp_data.json()
# print(type(users))
# print(resp_data.status_code)

# for user in users:
#     print(user['username'])
#     print(type(users))
# #task2 invoke rest apis and print all users in new json file
# import requests,json
# resp_data=requests.get('https://jsonplaceholder.typicode.com/users')
# users=resp_data.json()
# fp=open('user.json','w')
# json.dump(users,fp)
# print("new file created")
# print(type(fp))
# fp.close()
#using with keyword automatic resource mangement we should not to close the file pointer
import requests,json
resp_data=requests.get('https://jsonplaceholder.typicode.com/users')
users=resp_data.json()
with open('user.json','w') as fp:
    json.dump(users,fp)
print("new file created")
print(type(fp))

