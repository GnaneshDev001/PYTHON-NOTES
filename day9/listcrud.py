#list[]  methods
#create
eids=[101,102,103,104,102]
new_ids=[105,106,107,108]

#read
print(eids[0])
print(eids.count(101)) #count of re occurance of elements.
print(eids.index(102)) #return index of element of first occurance
#update
(eids.append(105)) #add element end of the list.
print(eids)

eids.insert(1,109)#insert element 109 @specified index.
print(eids)

eids.extend(new_ids)#to add the list elements by using new list
eids.extend({101,102,101})   #single elemnet can't update 
print(eids)
 
eids.reverse()#to reverse the object.
print(eids)
eids.sort()#sort in a-z. ascending order.
print(eids)
eids.sort(reverse=True) #sort in a-z. descending order.
print(eids)

#delete 
eids.pop() #remove last element from list and return it.
print(eids)

eids.remove(109) #remove specified eleement from list.
print(eids)

# eids.clear() #remove all elements from the list.
# print(eids)

# del eids  # delete the entire list from heap memeory.
# print(eids)

#copy function
eids=dat.copy()
print(eids)