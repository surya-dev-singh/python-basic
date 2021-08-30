#This method is used to update the dictionary with the specified key value pair.
#stu.update({105:'surya'})

stu={
    101:"Rahul",
    102:"raj",
    103:"surya"
}
print("original dict")
print(stu)
print(id(stu))
print()

stu.update({104:"python","address":101})
print("updated dict")
print(stu)
print(id(stu))
print()