#---default arguments---
#sometimes we mention default value to the formal arguments in function defination and we may not required to provide actual argument, in the case default argument will be used by formal arguments.if we do not provide actual arguments for formal arguments explicitly while calling a function then formal argument will use default value on the other hand if we provide actual argument then it will use provided value.
#------------------------------------------------------------------------
def show(name,age=27):
    print(f"name:{name} age:{age}")
show("surya")
#------------------------------------------------------------------------