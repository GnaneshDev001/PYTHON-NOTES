import csv
fp=open('emp.csv','w',newline="")#new line used bcs of line space is deleted.
cw=csv.writer(fp)
cw.writerow(['eid','ename','esal']) # write olny one row for header
data=[
    (101,'gana',45000),
    (102,'chandu',43000),
    (103,'madhu',42000)
]
cw.writerows(data)# write  multiple rows but consists tuple
print("new file")
fp.close()