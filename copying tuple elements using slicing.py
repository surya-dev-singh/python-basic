# we can copy/clone tuple elements using slicing method
a=(10,20,30,40,50)
b=a
print("A",a)
print("B",b)
print("id of a",id(a))
print("id of b",id(b))

print()
b=a[0:5] #here since data is same , therefore the id will remain the same.
print("A",a)
print("B",b)
print("id of a",id(a))
print("id of b",id(b))
