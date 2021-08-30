# nested list for loop
#firt type of nested list
a=[10,20,30,40,50,[1,2,3,4]]
n=len(a)
for i in range(n):
    if type(a[i]) is list:
        if len(a[i])>1:
            m=len(a[i])
            for j in range(m):
                print(i,j,a[i][j])
    else:
        print(i,a[i])
#second type of nested list.
# acessing list without index.
b=[[1,2,3,4,5],[6,7,8,9,0]]
for i in b:
    for c in i:
        print(c)
    print()
# acessing list with index
r=len(b)
for i in range(r):
    for j in range(len(b[i])):
        print(i,",",j,",","=",b[i][j])
    print()