# copy method
# This method is used to copy all the elements from the existing dictionary into a new dictionary.

stu={
    101:"rahul"
    ,102:"raj"
    ,103:"surya"
}
print("original dict:") 
print(stu)
print(id(stu))
print()

new_stu=stu.copy()
print("copied dict")
print(new_stu)
print(id(new_stu))
print()

#the new memory location is different 