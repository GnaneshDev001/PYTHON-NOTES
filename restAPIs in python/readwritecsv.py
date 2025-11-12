#read and write csv file:
import csv
fp=open('user.csv','r')
fp1=open('new.csv','w')
data=csv.reader(fp)
data1=csv.writer(fp1)
for row in data:
    data1.writerow(row)
fp.close()
fp1.close()




