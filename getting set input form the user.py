#getting set input from the user
a=set()
print(id(a))
n=int(input("enter the number of elements:"))
for i in range(n):
    el=input("Enter element: ")
    a.add(el)
print(a)
print(id(a))
#------------------------------------------------------------------------