from math import pi,sqrt,sin,cos,ceil,floor
print(pi)
print(sqrt(25))
print(sin(30))
print(cos(60))
print(ceil(4.2))
print(floor(4.8))

from random import randint,choice,choices#randint genetrates random integers in a range
for num in range(10):
    print(randint(100,999))
enames=["gana","balu","naga"] #choice  returns a random item from a list
print(choice(enames))
print(choices(enames,k=1))
from random import randrange #randrange generate a ransom integer btw two numbers
for i in range(1): 
    n=randrange(50,100,5)
    print(n)
from random import choice,choices
colors=["red","blue","green","yellow","black","white"]
user_input=input("type 'exit' to exit or press enter to get random colors:")
if(user_input=="exit"):
    print("exit")
else:
    print(choice(colors))