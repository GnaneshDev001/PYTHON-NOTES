#random 4 digit OTP generator
from random import randint #randint function generates random integers in a given range
for num  in range(10):
    print(randint(1000,9999))

numbers=range(1,100,-1)#range function with step value
for new in numbers:#this will not print anything as step value is negative
    print(new)