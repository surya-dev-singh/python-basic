# in c, java and some other programming language we pass value to function either by value or refernce widely known as "pass by value" and "pass by reference"
#in python , neither of these two concepts is applicable rather the value are sent to function by means of object refernce.
#when we pass value like number, string tuple or list to function, the refernce of these objects are passed to function.
#------------------------------------------------------------------------
def val(a):
    print(a,id(x))
    a=10
    print(x,id(x))
    #here different memory location will be created , because integer object are immutable(not modifiable).
x=10
val(x)
print(x,id(x))
#------------------------------------------------------------------------
def val(l):
    l.append(4)
    print(l,id(lst))
    #here no different location will we created , because list is mutable(changable).
lst=[1,2,3]
print(lst,id(lst))
val(lst)
print(lst,id(lst)) 
#------------------------------------------------------------------------
def val(b):
    print(b,id(lst))
    b=[11,12,13]
    #here new object and its new memory location will be created , but it is not accesible outside the function.
    print(b,id(lst))
lst=[1,2,3,4,5]
print(lst,id(lst))
val(lst)
print(lst,id(lst))
#-----------------------------------------------------------------------
#some important point:
#in python, values are passed to function by object references.
#if object is immutable(not modifiable) then the modified value is not available outside the function
#if the object is mutable(modifiable)then the modified value is availble outside the function.
#---imutable objects---
#integer
#float
#string
#tuple

#---mutable---
#list
#dictionary