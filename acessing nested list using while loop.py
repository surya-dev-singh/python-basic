a=[10,20,30,40,50,[1,2,3,4,5]]
##
#a=[1,2,3,4,[11,22,33],5,6,7,[44,55,66,77]] whith this list the below code will produce error. find the reason !!
i=0
while i<len(a):
    if type(a[i])==list:
        j=0
        while j < len(a[i]):
            print(i,j,a[i][j])
            j+=1
        i+=1 #it is important*
    else:
        print(i,a[i])
    i+=1
# extra thing
b=[[1,2],[3,4],[9],[5,6]]
for i in b:
    print(i[0])

# other type of nested list
b=[[1,2],[3,4],[5,6],[7,8]]
i=0
while i < len(b):
    j=0
    while j < len(b[i]):
        print(i,j,b[i][j])
        j+=1
    i+=1


