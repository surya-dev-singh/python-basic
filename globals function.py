#---globals() function---
    #the function return a table of current global variable in form of dictionary.we use this if we want to use global as well as local variable in our function without affecting actual value of global function.
#------------------------------------------------------------------------
a=50
def show():
    a=10
    print("local variable A:",a)
    x=globals()['a']#we can not do like this x=global a
    print(x)
show()
print("global variable :A",a)
print(globals())
#---------------------------------END------------------------------------