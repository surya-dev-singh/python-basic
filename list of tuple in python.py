#list of tuple
a=[10,20,(30,40)]
print("original list",a)
print(id(a))
print(type(a))
print()

#appending new tuple

a.append((50,60))
print("after appending a tuple",a)
print(id(a))
print(type(a))
print()

#acessing list of tuples using for loop

for i in range(len(a)):
    if type(a[i]) is tuple:
        if len(a[i])>1:
            for j in range(len(a[i])):
                print(i,j,a[i][j])
    else:
        print(i,a[i])

print("--------------------------------------------------------")

b=[(10,20),(30,40)]
print("original list B",b)
print(id(b))
print()

b.append((50,60))
print("after appending a tuple",b)
print(id(b))

for i in range(len(b)):
    for j in range(len(b[i])):
        print(i,j,b[i][j])
    print()
