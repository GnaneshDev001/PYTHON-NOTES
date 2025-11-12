#read data.txt file and
#write data into new file in wish.txt file
fp=open('wish.txt','w')
data="hello good morning"
fp.write(data)
print("new file created successfully")
fp.close()