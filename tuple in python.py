#---tuple---
#a tuple contains a group of elements which can be same or different types. Tuple are immutable .
#It is similar to list bur tuples are read-only which means we can not modify it's elements.
#Tuples are used to store data which should not be modified 
#It occupies less memory comapare to list.
#Tuples are represented using parenthesis ().
#eg:- a=(10,20,30,40,50,60,70,80,90,100)
#------------------------------------------------------------------------
#creatinig an empty tuple
a=()
#------------------------------------------------------------------------
#creating tuple
#we can create tuple by writing elements separated by commas inside parenthese.
#-----------------------------------------------------------------------
##with one element
b=(10,) # If i have written it like this b=(10), it is not tuple , it wil be treted as int.
c=(10)
print(type(b))
print(type(c))
#------------------------------------------------------------------------
##with different elements
d=(10,20,30,40,50)
e=(10,20,30,40,50,"surya",10.7)
#------------------------------------------------------------------------
##without parenthesis 
#we can make tuple without parantheses , it will by default treates as tuple.
f=10,
print(type(f))
g=20,40,"surya"
print(type(g))
#------------------------------------------------------------------------
##tuple function
l=[1,2,3,4]
print(type(tuple(l))) # we can not change an int to tuple because int is not iterable.
k="surya"
print(type(tuple(k))) #since string is iterable object we can convert it to tuple.