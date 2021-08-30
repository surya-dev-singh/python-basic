#---global keyword---
    #if local variable and global variable has same name,then function by default refers to the local variable and ignore the global variable.it means global variable is not accessible inside the function but possible to access outside of the function.
    #in this situation , if we need to acess global variable inside the function we can acess it using global keyword followed by variable name.
#------------------------------------------------------------------------
a=50
def show():
    a=10
    print("A: ",a)
show()
#------------------------------------------------------------------------
i=0
def show():
    global i
    i+=1
    print("I: ",i)
show()
print(i)
#--------------------------------------END-------------------------------
