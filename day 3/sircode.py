eid=101
esal=45000.45
ename="Rahul"
c=10+20j
avail=True 
eids=[101,102,103,104] #list
unames=('RG','SG','Priya','Modi')#tuple
numbers={10,10,10,20}#set
emp={            #dictionary
    'eid':101,
    'ename':'Rahul'
}
b = bytes([10,20,30,255]) 
ba=bytearray([10,20,30,255])
fz=frozenset({10,10,10})
r=range(100)
n=None 

print(type(eid))    #<class,int>
print(type(esal))   #<class,float>
print(type(ename))  #<class,str>
print(type(c))      #<class,complex>
print(type(avail))  #<class,bool>
print(type(eids))   #<class,list>
print(type(unames))   #<class,tuple>
print(type(numbers))   #<class,set>
print(type(emp))   #<class,dict>
print(type(b))   #<class,bytes>
print(type(ba))   #<class,bytearray>
print(type(fz))   #<class,frozenset>
print(type(r))   #<class,range>
print(type(n))   #<class,NoneType>