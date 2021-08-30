#passing and returning a list 
def show(l):
    print("funtion output")
    print(l)
    print(type(l))
    for i in l:print(i)
    print("funtion output close")
    return l
from numpy import arange
a=arange(0,9)
print(type(a))
print(type(show(list(a))))

