enames=["gnana","chandu","balu","kalyan","reddy"]
print(len(enames))
from random import choice #importing choice function from random module
print(choice(enames))#choice function returns a random item from a list

from random import choices
print(choices(enames,k=3))#choices function returns k  no of random items from a list

print(floatrandom(0,1))#floatrandom function returns a random float number between 0 and