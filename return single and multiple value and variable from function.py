#---return statment---
#return statements can be used to return something from function . in python it possible to return one or more variables/values.
#return(variable or expresion)
#-----------------------------------------------------------------------
def add():
    x=10
    y=20
    c=x+y
    return c #return(c)
sum=add()
print(sum)
##
def sub():
    x=10
    y=20
    return(x+y,y-x)
sum1,sub=sub()
print(sum1)
print(sub)
#------------------------------END---------------------------------------