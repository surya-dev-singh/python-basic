#---math module---
# it is module that contains several functions to perform mathematical operations. if we want to use it we have to import it first from math import *
#---some of the functions of maths module.
#1.floor(n):-decrease n value to the previous integer value . if n is integer, then same is returned.
#2.ceil(n):-raise n value to the next higher integer . if n is integer,then same value is returned.
#3.fabs(n):-returns absolute value or positive qrantity of n .
#4.factorial(n):-returns factorial value of n.
#5.sqrt(n):-returns a positive squre root  of n 
#6.pow(n,m):-returns a n value of to the power m.
#7.sin(n):-returns a sin of n
#8.cos(n):-returns a cos of n
#9.tan(n):-returns a tanget of a function.
#10.gcd(n,m):-returns the gretest common divisior of the integer a and b . if either a or b is nonzero , then the value of gcd(a,b) is the larget positive integer that devide both a,b. the gcd(0,0) returns 0.
from math import *
print(floor(6.5))#this function will show priviouse value, here it is 6 , means form 6 it has become 6.5
print(ceil(7.2))#this function will show forword value, here it is 8 ,means from 7.2 it will become 8.
print(sqrt(49))
print(factorial(5))
print(pow(5,2))
print(sin(pi/2))