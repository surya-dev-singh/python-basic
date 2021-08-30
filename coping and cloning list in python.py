#---copying list---
#copy() meehod is used to copy all the elementd og a list to another list.When we copy a list swparate coopy of all the elements is stored in another list.Both the list are independent.
a=[1,2,3,4,5,6]
b=a.copy()
print(a,id(a))
print(b,id(b))
#here we are forcing python to create two different memory location for the same value of the object.

#---cloning list---
#We can clone a list into another list using slicing.When we clone a list a separate copy ojall the elements is stored in another list. Both the list are independent.
c=[10,20,30,40]
d=c[:] # remember this is is cloning
print(c,id(c))
print(d,id(d))
#in both the cases modification in one will not affect the other.

#---------------------------END---------------------------------------