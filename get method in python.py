#this method returns the value of the specified key.
#if key is not found then it will return none or deafault value.
#syntax: dict.get(key,defaultvalue)

stu={101:"rahul",102:"raj",103:"surya"}
print("original dictionary")
print(stu)
print()

print(stu.get(101))
print(stu.get(1))
print(stu.get(110,"not found"))