data=[11,22,33,44,55,66,77,88,11]
dat=[1,2,3]
#read
print(data)
print(data.count(11))
print(data.index(55))
#update
data.append(10)
print(data)
data.insert(1,9)
print(data)
data.extend(dat)
print(data)
data.sort()
print(data)
data.sort(reverse=True)
print(data)
data.reverse()
print(data)
#delete
data.pop()
print(data)
data.remove(77)
print(data)
# data.clear()
# print(data)
del data[1]
print(data)