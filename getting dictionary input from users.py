a={}
n=int(input("enter the number of elements:"))
for i in range(n):
    k=input("enter key: ")
    v=input("enter value: ")
    a.update({k:v})

print(a)