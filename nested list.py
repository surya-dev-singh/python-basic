#----nested list---
# list inside a list is called nested list
# import array
a=[10,20,30,40,[1,2,3,4]]
print(a)
print(a[0])
print(a[4])
print(a[4][2])
a[1]=100
a[4][0]=900
print(a)
a[4]=300
print(a) 
#-------------------------
from numpy import arange
b=(list(arange(0,10)))
c=[1,1,1,1,b]
print(c)
# #-------------------------
d=[[1,2,3,4],[10,20,30,40]]
print(d)
print(d[0][0])
print(d[1][3])
print(d[0][2])
print(d[1][2])
d[0][0]=3200
print(d)
d[1]=29
print(d)
print("*******")