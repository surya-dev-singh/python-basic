#---higher order function---
#map()function:
#This function executes a specified function on each element of the iterables(sequence) and perhaps changes the element. 
#syantax:
#map(function_name,iterable)
#function_name: its name of a function which perform an operation on all the elements of the sequence and modified element are returned which can be stored in another sequence.
#iterable:iterable may be either a sequence , list, string, tuple, a container which support iteration, or an iterator. 
a=[10,20,30,40,50]
def inc(n):
    return n+2
r=map(inc,a) 
print(r)
print(type(r))
#since map object is iterable , we will use for loop on it.
for i in r:
    print(i)
#for handy purpose we can use it like this:
print("*"*10)
b=[1,2,3,4,5,6,7,8,9,10]
for i in map(lambda x : x*3,b):print(i)
#-----------------------------END-----------------------------------