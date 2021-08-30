# we can delete an item of dictionary or entire dictionary using del keyword.

stu={
    101:"rahul",
    102:"raj",
    103:"arpit"
}
print("before deletion:")
print(stu)
print(id(stu))
print()

del stu[102]
print("after delition:")
print(stu)
print(id(stu))
print()

del(stu)
print(stu) #this will give error, because we have deleted it.
