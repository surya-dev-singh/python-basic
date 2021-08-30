# getting input from the user:
#first getting input in list and then convert it in tuple, this might cause memory issue if you have lot of data.
a=[]
n=int(input("enter the number of element: "))
for i in range(n):
    a.append(int(input("enter element: ")))
print()
print(a)
print(type(a))
print()
a=tuple(a)
print(a)
print(type(a))