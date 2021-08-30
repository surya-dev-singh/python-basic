#first lets make dictionary without any comprehension:
dict1={}
n=0
while (n<10):
    dict1[n]=n*2
    n+=1
print(dict1)

#now using comprehension
dict2={n:n*2 for n in range(10)}
print(dict2)
print()
#now using if statement:
dict3={n:n*2 for n in range(10) if n%2==0}
print(dict3)
print()

dict4={n:n*2 for n in range(20) if n%2==0 if n%3==0}
print(dict4)

print("^^^^^^^^^^^^^^^^^^^^^")
dict5={n:(n if n%2==0 else "invalid") for n in range(10)}
print(dict5)

#-----------extra but important------------------
#extra concept how to convert list of tuples to dictionary:
lst=[(101,"rahul"),(102,"raj")]
dict1={k:v for k,v in lst} #comprehension







