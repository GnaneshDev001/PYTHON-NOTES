#Program to generate a random integer between 1 and 100
from random import randint
print(randint(1,100))

import random
print("random numbers from 1 t 100")
for i in range(1):
    ran=random.randint(1,100)
    print(ran)

#program to generate a random float number between 0 and 1
from random import uniform
num = uniform(0,1) #uniform function generates float numbers in a given range
print(num)

import random
print("float number from 0 t0 1")
for i in range(0,1):
    ran=random.random()
    print(ran)

#Generate a random number between 50 t0 100 with step value 5
from random import randrange
print(randrange(50,100,5)) #randrange function generates numbers in a given range with step value.

print("random number from 50 t0 100 with step value 5") 
for i in range(1):
    ran=randrange(50,100,5)
    print(ran)

#create a list of 10student names.randomly select on student as the "class monitor"
names=["gnana","chandu","balu","kalyan","reddy","srinu","mahi","vijay","ajay","arjun"]
from random import choice
print("class Monitor","-",choice(names))
#Randomly shuffle the list of students and print the new order
names=["gnana","chandu","balu","kalyan","reddy","srinu","mahi","vijay","ajay","arjun"]
from random import choices
print(choices(names,k=10))
#Generate a list of colors Allow the user to exit the program by typing 'exit'.
from random import choices
colors=["red","blue","green","yellow","black","white"]
user_input=input("type 'exit' to exit or press enter to get random colors:")
if(user_input=="exit"):
    print("exit the program")
else:
    print(choices(colors))
#Generate a random number between 1 and 49, simulating a lottery draw
from random import randint
print("lottery draw numbers are:")
for i in range(6):
    print(randint(1,49))

