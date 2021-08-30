#tuples of list
a=(10,20,[30,40])
print("original tuple A:",a)
print(id(a))
print(type(a))
print()

#modifying lists
a[2][0]=90
print("after modifying list:",a)
print(id(a))
print()

#acessing Tuple of lists using for loop:
for i in a:
    if type(i) is list:
        for j in i:
            print(j)
    else:
        print(i)

print()

#other type of tuple of list
b=([10,20],[30,40])
print("original tuple b",b)
print(id(b))
print()
b[0][0]=80
print("after modification: ", a)
print(id(b))
print()

#acessing the elements of tuple of list
for i in b:
    for j in i:
        print(j)
    print()