#we can add a new elementss to set using add() method.
a=set()
a.add("python")
print(a)


b={10,20,"surya",40}
b.add("hello")
print(b)

#------------------------------------------------------------------------

#we can add multiple elements to set using update() methods.
#the update() method can take tuples , list, string or other sets as its arguments.

c={1,2,3,"s"}
c.update([12,34]) #here we are giveing what we want in our set as list, but set will show value inside list , not a list.
print(c)