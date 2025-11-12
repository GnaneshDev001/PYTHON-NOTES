from random import randint
print(randint(1,10))

for i in range(100):
    num=randint(1,100)
print(num)

from random import uniform
num=uniform(0,1)
print(num)

import random
for i in range(0,1):
    num=random.random()
print(num)

from random import randrange
# for i in range(10):
num=randrange(50,100,5)
print(num)
from random import choice,choices
names=["gnana","chandu","balu","kalyan","reddy","srinu","mahi","vijay","ajay","arjun"]
print("class monitor-",choice(names))
print(choices(names,k=3))
user_input=input("type 'exit' to exit the program or press enter to get random colors")
if(user_input=="exit"):
    print("exit to program")
else:
    print(choice(names))