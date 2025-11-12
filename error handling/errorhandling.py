# a=int(input("enter a first function :"))
# b=int(input("enter a second function :"))
# print(a/b)
# # case:2 print(a/b)a=10;b=0; could not execute #Zerodivision error
# # case:3 print(a/b)a=10;b=rahul; could not execute #valueError

try:
    a=int(input("enter a first function :"))
    b=int(input("enter a second function :"))
    print(a/b)
except ValueError as err:
    print(err)
except ZeroDivisionError as err:
    print(err)
print("ge")