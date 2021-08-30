#---list--
    # a list represent a group of elements .
    # list are very similar to array but ther is major difference , an array can store only one type of elements whereas a list can store different types of elements.
    # list are mutable so we can modify its elemets, without affection privious memory location.
    # list ca store different types of element which can be modified.
    # list is represent by []
###list are dynamic means size is not fixed.
a=[1,2,3,4,5,6,7,8]
print(a)
print(a[-1])
print(a[4])
print("#########")
print("memory location before any changes",id(a))
a[0]=10
print("memory location after changes in a",id(a))
print("#########")
#accessing list using for loop
for i in a:
    print(i)
print("/////")#other way
for i in range(len(a)):
    print(i,":",a[i])
print("/////")
#accessing list using while loop
m=0
while m < len(a):
    print(a[m])
    m+=1
