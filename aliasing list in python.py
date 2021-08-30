#---aliasing list---
#Aliasing means giving another name to the existing object. It doesn't mean copying.
a=[10,20,30,40]
b=a
#it is not coppying thing from a , just giving it another name , means modification in a will will affect b and vice versa.
print(a,id(a))
print(b,id(b))

a[0]=1
print("after modification")
print(a,id(a))
print(b,id(b))

#--------------------------------------END-------------------------------