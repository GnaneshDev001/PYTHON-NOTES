def wish():
    eid=101;
    print(type(eid))
    print(eid)
    
    #print(C) # C is not defined, will raise an error
ename='gnana'
print(ename)
print(type(ename))
esal=23.5
print(esal)
print(type(esal))
complex=10+20j
print(complex)
print(type(complex))
Value=True
print(Value)
print(type(Value))
eids=[10,2.2,True,] #undefined,null not allowed
print(eids)
print(type(eids))
unames=(11,102,True,'gnana') #undefined,null not allowed
print(unames)
print(type(unames))
number={'gnana','mahi',10,10,20} #undefined,null not allowed
print(number)
print(type(number))
dic={
    "eid":101,
    "ename":'hello',
    "esal":42000,
}
print(dic)
print(type(dic))
b=bytes([10,20]) #string values not allowed
for val in b:
    print(val)
print(type(b))
ba=bytearray([10,20]) #string values not allowed
for use in ba:
    print(use)
print(type(ba))
fs=frozenset={1,23.5,True}
print(fs)
print(type(fs))
r=range(50)
print(r)
print(type(r))
n=None
print(n)
print(type(n))

wish()


b=bytes([10,20]) #string values not allowed
for val in b:
    print(val)
print(type(b))
ba=bytearray([10,20]) #string values not allowed
ba[0]=30
for use in ba:
    print(use)
print(type(ba))