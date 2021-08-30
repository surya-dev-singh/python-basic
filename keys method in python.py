#This method returns a sequence of keys from the dictionary.
#syntax: dict.keys()
stu={101:"a",
    102:"b",
    103:"c"
    }
print("original dict:")
print(stu)
print()

k=stu.keys()
print(k)
print(type(k)) #this will returns dict key objects.
#this object is iterable.
for i in k:
    print(i)

#we can also do type converstion, and perform other things.
lst=list(k)
print(type(lst))
print(lst)
for i in lst:
    print(i)
