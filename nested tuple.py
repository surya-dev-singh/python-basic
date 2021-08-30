# A tuple within another tuple is called as nested tuple or nesting of a tuple.
a=(10,20,30,(50,60))
print(a)
print(a[0])
print(a[3][0])
print()
b=((10,20,30),(40,50,60))
print(b)
print(b[0][0])
print("*"*25)
# acessing nested tuple using for loop:
#case I:
a=(10,20,30,(50,60))
for i in range(len(a)):
    if type(a[i]) is int:
        print(a[i])
    else:
        if len(a[i])>1:
            for j in range(len(a[i])):
                print(a[i][j])
print("*"*25)
#case II:
a=((10,20,30),(40,50,60))
# without index:
for r in a:
    for c in r:
        print(c)
    print()
print("%"*15)
# with index:
for j in range(len(a)):
    for k in range(len(a[j])):
        print(a[j][k])
    print()
print("*"*25)
#acessing nested tuple using while loop:
#case I:
a=(10,20,30,(50,60))
i=0
while i < len(a):
    if type(a[i]) is tuple:
        if len(a[i])>1:
            j=0
            while j<len(a[i]):
                print(a[i][j])
                j+=1
            i+=1
    else:
        print(a[i])
        i+=1
#case II:
print("*"*25)
a=((10,20,30),(40,50,60))
i=0
while i<len(a):
    j=0
    while j<len(a[i]):
        print(a[i][j])
        j+=1
    i+=1
    
