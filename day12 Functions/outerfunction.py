# def outer():
#     print("gm")
#     def inner():
#         print("hello")
# outer() #NameError: name 'inner' is not defined
# inner()
#invoke inner function using reference from outer function       
def outer():
    print("good morning")
    def inner():
        print("hello")
    return inner
inn=outer()
inn()
#invoke inner function reference outside outer function
def calc():
    def add():
        print("addition")
    def multi():
        print("multiplication")
    return multi
ran=calc()
ran()
print(type(ran))
# print(ran)
#invoke of two inner functions from outer function
def calc():
    def add():
        print("addition")
    def multi():
        print("multiplication")
    return multi,add
ran=calc()
print(type(ran))
ran[0](),ran[1]()
