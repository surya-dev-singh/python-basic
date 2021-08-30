#---lambda function---
    #a function without a name is called as lambda function. it is also known as anonymouse function.
    #anonymouse function are not defined using def keyword rather they are defined using lambda keyword.
    #syntax:-
    #lambda  arguments_list:expression
    #here argument_list can be 0 or as many as we want,but expression should be only 1.
#---how lambda function work---
    #actually lambda function function returns a function , which we can store it in function variable  and we call it.
##in lambda function no need to write return statement
##lamda can only contain expression and can't include statement in its body.
## you can use all type of actual arguments.
###lambda function are commonly use when you want to pass function as argument to heigher-order functions,that is , functions that takes other function as there argument.
#------------------------------------------------------------------------
def show(x):
    print(x)
show(5)
#-----------------------------------------------------------------------
show=lambda x:print(x)
show(5)
#------------------------------------------------------------------------
add=lambda x,y:x+y
print(add(5,6))
#------------------------------------------------------------------------
add_sub=lambda x,y:(x+y,x-y) #here dont think we are writting more than one expression , like in normal function we can return multiple values written in "return()", similarly it is just returning multiple value , but in order to do that we should write it in (), if we write more that onre expression without () it will become more than one expression and lambda function only support 1 expression
a,s=add_sub(5,2)    #tuple unpacking
#-----------------------------------------------------------------------
    #it will give error
# new=lambda x,y:x+y,y-x
# k,l=new(5,6)
#------------------------------------------------------------------------
# use of all actual argument:
add=lambda x,y=3:x+y
print(5)#(default argument)
#-----------------------------------------------------------------------
add=lambda x,y,z,q:x+y+z+q
print(add(z=10,q=11,y=12,x=3))# here order is not necessary (position argument)
#------------------------------------------------------------------------
add=lambda *args:print(args)
add(4,5,6,7,8,9,10) #(variable length keywors argument)
#------------------------------------------------------------------------
add=lambda **kwargs:print(kwargs.values())
add(name="surya",age=10,location="india",friend="nobody")
#------------------------------------------------------------------------
