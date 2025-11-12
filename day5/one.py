
#create
enames=['RG','SG','PG','NM']
#read
print(enames)
print(type(enames))  #<class,list>
#how to read list elements using indexing
print(enames[0])
print(enames[1])
print(enames[2])
print(enames[3])
#print(enames[8])  #IndexError

#update
enames[3]="Modi"
#enames[300]="Nanditha" #IndexError:
print(enames)
#delete
del enames[3]
print(enames)
