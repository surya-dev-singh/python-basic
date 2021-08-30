#---higher order function---
#reduce function()
#This function is used to reduce a sequence of element to a single value by proccessing the elements according to a function supplied. It returns a single value.
#this function is part of functool module, so you have to import it before using it.
#syntax:
# from functools import reduce
# reduce(function_name,sequence)
#-----------------------------------------------------------------------
from functools import reduce
a=[10,20,30,40,50]
print(reduce(lambda n,m: n+m , a)) # here the value of n initially is 0 and value of m is the first value of  our iterable a . we can also provide initial value in reduce function.and can also provide our iterable in reduce funtion itself.
print(reduce(lambda m,n: m+n,[1,2,3],0))
# here 0 is initial value of n in our iterable [1,2,3]
