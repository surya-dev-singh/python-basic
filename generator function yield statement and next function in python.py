#---iterable---
# iterable is that object in which __iter__ or __getitems__ method are defined.means  it is that object , which can give us iterator.
#---iterator---
#iterator are  those object in python in which next object is defined.
#---iteration---
#iterating iterable object , or fetching their next object is called iteration.
#------------------------------------------------------------------------
l=[10,20,30,40] #list is itrable object , not itself a iterator
a=iter(l) # but iterable object can giver us iterator, so we use iter function on our iterable(here list) to produce iterator
print(next(a)) # now we can use next function on our produce iterator.
#------------------------------------------------------------------------
b=[10,20,30,40]
a=iter(b)
i=0
while i<=len(b)-1:
    print(next(a))
    i+=1
print(list(a)) # here list is empty means in our iterator object there is nothing , so on our iterator object we could iterate only once

#---generator---
#generator are function that returns a sequence of values . We use yield statement to return the value frim function.
#---yield statement---
#yield statement retuns the elements from a generator function into a generator object.
#eg: yield a
#---next()---
# This function is used to retrieve element by element from a generator object.
#every generator is build by calling a function that has one or more than one yield statements
# syntax: next(gen_obj)

#generator object is not iterable.
#every generator is iterator , but not every iterator is generator.
#generator are those function on which we iterate only once., indirectly iterator are those object which which we can iterate once.

def disp(a,b):
    yield a
    yield b
result=disp(10,20) #here our result variable is iterator.
print(result)
print(type(result)) 
print(next(result))
lst=list(result)
print(lst)
print(type(lst))
print(id(lst))
print(id(result))
#------------------------------------------------------------------------
def show(a,b):
    while a<=b:
        yield a
        a+=1
new_result=show(1,5)
print(new_result)
print(type(new_result))
print(next(new_result))
# an iterator is is ieterable, and an iterable can produce iterator
for i in new_result:
    print(i)
    
# advantage of using iterator or genrator function, they are memory eficient, means one element out of your iterator or iterable is take, once it is use its discarded from memory , so , they are memory efficient.