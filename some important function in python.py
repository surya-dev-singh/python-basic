#id() function---------->

#this funciton returns the "identity" of an objects.

#The identity is an integer which is guaranteed to be unique and constant for this object during its lifetime.

#Two objects with non-overlapping lifetimes may have the same id() value.

#Cpython implementation detail -- This is the address of the objects in memory.

#type() function----------->

#this function returns type fo the objects

#getsizeof() function---------->

#This function returns the size of an objects in bytes.

#The objects can be any type of object.

#all built-in objects will return correct result, but this does not have to hold true for third party extension as it is implementation specific.

#only the memory consumption directly attributed to the object  is accounted for, not the memory consumption of objects it refers to.

#Thsi is part of sys module so you have to import sys module before using this function.
from sys import getsizeof
a=[1,2,3,4]
b=(1,2,3,4)
c={1,2,3,4}
print(getsizeof(a),getsizeof(b),getsizeof(c))


#int() function--------->

#this function returns an integer objects or returns 0 if no arguments are given .

#float() function----------->

#thisfunction returns an floating point number object.

#str() function----------->

#this function returns str version of objects.

#list() function---------->

#rather than being a function , list is actually a mutable sequence type. This can be used in type casting to convert iterable to list.

#tupel() function------>

#rather than beign a function , tuple is actually an immutable sequence type. This can be also used in type casting to convert iterable to tuple.

#set() function ---------->

#this function returns a new set objects , optionally with elements taken from iterable. This can be also used in type casting to convert iterable to set.

#dict() function------------>

#This function creates a new dictionary . this can be also used in type casting to convert iterable to dict.
#syntax:- dict(**kwarg)
print()
a=[(101,"rahul"),(102,"raj")]
print(a)
new_a=dict(a)
print(new_a)

#len() function--------->

#This function returns the length (the number of items ) of an objects. 
#this argument may  be a squence (such as string , bytes, tuple, list, or range) or a collection (such as dictionary , set or frozen set)
#frozen set are just immutable version of set. we can create them using frozenset() function.

#min() function---------->

#This function returns the smallest item in an iterabl or the smallest of two or more arguments.

#if one positional arguments is provided, it should be an iterable.The smallest item in the iterable is returned. if two or more positional arguments are provided, the smallest of the positional arguments is returned.

#max() funciton---------->

#just opposite of min () !! , i know you get it !!

#sorted()  function---------->

#This function returns a new sorted list from the items in iteable.
#this will always returns a list
print()
a=[2,3,4,1,5]
print(sorted(a))
print()
a={3,5,2,5,2,7}
print(sorted(a))



#membership operator--------->

#in, not in
#these operator checks, wheter something is there in our iterable or not.



