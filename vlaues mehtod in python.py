# this gives all the values of specified dictioanry.
stu={
    101:"rahul",
    102:"raj",
    103:"surya"
}
print("orginal dictionary")
print(stu)
print(id(stu))
print()

v=stu.values()
print(v)    
print(type(v)) # dict_value type object is iterable
for i in v:
    print(i)