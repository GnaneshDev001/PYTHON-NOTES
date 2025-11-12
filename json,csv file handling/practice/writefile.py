fp=open('data.txt','r')
data=fp.read()
print(data)
fp.close()

##################
fp=open('data.txt','r')
fp1=open('wish.txt','w')
data=fp.read()
fp1.write(data)
print("vivek pookie")
fp.close()
fp1.close()
