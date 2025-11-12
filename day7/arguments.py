#keyword arguments
def calc(a,b):
    print(a-b)
calc(a=100,b=200)    
calc(b=200,a=100)    
#positional arguments
def wish(a,b):
    print(a-b)
wish(100,200)    
wish(200,100)   
#default arguments
def void(a,b,c=100):
    print(a+b+c)
void(100,200,300)    
void(200,100)   
#variable length argumetnts
def run(a,*b):
    print("a:",a,"b:",b)
run(10,20)
run(10,20,30)
run(10,20,30,40)
run(10,20,30,40,50)