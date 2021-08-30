# since dicitionary is mutable objects, so we can change it , without affection id number/memory address.
#we can modify the existing value of key by assigning a new value.

stu={
    101:"rahul",
    102:"raj",
    103:"surya"
}
print("before modification")
print(stu)
print(id(stu))
print()

stu[102]="python"
print("after modification")
print(stu)
print(id(stu))
print()