#This method is used to remove the item which was last inserted into the dictionary.
#It returns the remove item in the form of tuple, pairs are returned in LIFO (last in first out) order.

stu={
    101:"rahul",
    102:"raj",
    103:"surya"
} 
print("original dictionary")
print(stu)
print(id(stu))
print()

poped=stu.popitem()
print("after removing item")
print(stu)
print(id(stu))
print(poped)
print()