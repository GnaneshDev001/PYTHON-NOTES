
import data #importing module
print(data.eid)#print the eid variable from data module
data.login()#calling login function from data module

from data import eid,login,Account#importing specific items from data module
print(eid)
from data import *#importing all items from data module
login()
from data import eid as empid#importing with alias
print(empid)
