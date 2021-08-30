#passing Tuples to function
def show(t):
    print(t)
    print(type(t))
    for i in t:
        print(i)
t=10,20,30,40,"surya"
show(t)