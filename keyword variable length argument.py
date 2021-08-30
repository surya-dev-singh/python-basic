#---keyword variable length argument---
    #  is an argument that can accept any number of vlaues provided in   form of key-value pair. the keyword variable length srgument is written with ** symbol. it stores all the value in a dictionary in the form of key-value pair.
#------------------------------------------------------------------------
def add(**kwargs):
    z=kwargs['a']+kwargs['b']+kwargs['c']
    print("addition",z)
add(a=10,b=8,c=6)
#------------------------------------------------------------------------
def add(a,**kwargs):
    z=a+kwargs['b']+kwargs['c']
    print("addition",z)
add(10,b=8,c=6)

