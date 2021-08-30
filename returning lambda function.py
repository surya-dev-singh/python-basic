#we can return a lambda function from function
def add():
    y=20
    return(lambda x:x+y)
a=add()#here a is actually having lambda function
print(a(10))
print(a)
print(id(a))
#--------------------------END------------------------------------------