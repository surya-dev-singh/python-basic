from array import array
def show(ar):
    print(ar)
    print(type(ar))
    for i in ar:
        print(i)
    return ar
a=array('i',[1,2,3,4,5,6])
y=show(a)
print()
print(y)
for i in y:
    print(i)
import numpy
j=numpy.array([10,20,30,40,50])
def new(arr):
    print(arr)
    print(type(arr))
    for i in arr:
        print(i)
    return arr
z=new(j)
print("///")
for i in z:
    print(i)
#-----------------------END----------------------------------------
