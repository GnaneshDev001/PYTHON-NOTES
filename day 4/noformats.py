a=15      #Decimal Format
b=0b1111  #Binary Format
c=0o17    #Octal Format second values represents number format.
d=0xf     #HexDecimal Format

print(a)   #15
print(b)   #15
print(c)   #15
print(d)   #15

print(type(a))  #<class,int>
print(type(b))  #<class,int>
print(type(c))  #<class,int>
print(type(d))  #<class,int> 

# to print number in a different formats
a=15
print(int(a))   #15
print(bin(a))   #0b111
print(oct(a))   #0o17
print(hex(a))   #0xf

# to print individual numbers
a,b,c=100,200,300
print(a)
print(b)
print(c)


eids=101,102,103,
print(eids)        #(101,102,103) 
print(type(eids))  #<class,tuple>