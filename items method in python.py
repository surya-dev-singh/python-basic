#Thsi method returns an objects that contains key-value pairs of dictionary.
#The pair are stored as tuples in the objects.

stu={
    101:"a",
    102:"b",
    103:"c"
}
print("original dict")
print(stu)
print()

it=stu.items() #this will returns an objects that has key value pair.
print(type(it)) #it is dict_tems(name of the object)
#this method is iterable.
print(it)
print()
for i in it:
    print(i)
#we can also type cast dict_items method to list and do the other things.
print()
lst=list(it)
print(lst)
type(lst)
print()

print(lst[0][0])
print()
for r in lst:
    for c in r:
        print(c)
