#---local variable---
    #the variable which are declare inside a function is called local variable.local variable scope is limited to only where it is created.it means local variable values is available only if that variable is not outside of that function.
#------------------------------------------------------------------------
def add(y):
    x=10
    print(x)
    print(x+y)
add(20)
# print(x)# this will  generate error because x is local variable .