# write py script,read user.csv file
# and print all user names
import csv
with open('user.csv','r') as fp:
    user_reader=csv.reader(fp)
    users=list(user_reader)
    # print(type(user_reader))
    #print(user_reader)
    for user in users[1:]:
       # print(type(user))
        print(user[1])
        



