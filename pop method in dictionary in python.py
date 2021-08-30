#pop() Method
#This method is used to remove the items with specific key.
# we can also use del key word.
#it returns the remove item's value.
#if key is not found the the default value is returned.
#If key is not found and default value is not defined the it shows KeyError.
#syntax: dict_name.pop(key,default_value)
stu={
    101:"rahul",
    102:"raj",
    103:"sonam"
}
print("original dictionary")
print(stu)
print(id(stu))
print()

poped=stu.pop(101,"not found")
print(stu)
print(id(stu))
print(poped)

poped1=stu.pop(1024,"not found")
print(poped1)