eids={101,102,103,104}
#create
uids=eids.copy()#create a shallow copy of the set.
print(uids)
#read 
#eids.count(101) #AttributeError: 'set' object has no attribute 'count'.

#update
eids.add(105)#add a specific element to the set.
print(eids) 

eids.update({106,107})#add multiple elements to the set.
print(eids)
#delete
eids.pop() #removes  (random element)and returns an arbitrary  element from the set.
print(eids)
eids.remove(107) #removes a specific element from the set. raises KeyError if the element is not found.
print(eids)
eids.discard(108) #removes a specific element from the set.if the element is not found no error is raised.
print(eids)
eids.clear() #removes all elements from the set.
print(eids)
