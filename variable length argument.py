#---variable length arguments---
    #variable length argument is an arguments that can accept any number of values.the variable length argument is written * symbol.it store all value in tuple.
#------------------------------------------------------------------------
def add(*args):
    z=args[0]+args[1]
    print("addition",z)
add(5,2)
#------------------------------------------------------------------------
def add(x,*args):
    z=0
    for i in args:
        z+=i
    z+=x
    print("addition",z)
add(5,32,3)
# here 5 got its place in x , and 32,3 got in args
#---------------------------------END------------------------------------

