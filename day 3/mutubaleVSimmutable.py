#b=bytes([10,20,30,40])
#b[0]=100 # This will raise an error because bytes are immutable
#print(b)

ba=bytearray([10,20,30,40])
ba[0]=100 # This is valid because bytearray is mutable
print(ba)

