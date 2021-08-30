#---decorator function---
    # a decorator function is a function that accepts a function as parameter and returns a function.
    #a decorator takes the result of the function, modifies the result and return it.
    #in decorator, functions are taken as the argument into anothr function and then called inside the wrapper function.
    #we use @function_name to specify a decorator to be applied on another function.
#------------------------------------------------------------------------
# def decor(fun):
#     def inner():
#         print("INNER FUNCTION:before enhancing")
#         fun()
#         print("INNER FUNCTION:after enhancing")
#     return inner
# def num():
#     print("we will use this function")
#     print("and we will enhance this in decorator")
# result_fun=decor(num)
# result_fun()
#------------------------------------------------------------------------
##- here instead to writing lst two line we can use @ symbol instead .
#------------------------------------------------------------------------
# def hello(newfun):
#     def inner():
#         print("IN:hello")
#         newfun()
#         print("IF:byee")
#     return inner
# @hello
# def newnum():
#     print(" i am sam")
#     print("no, my name is sam")
# newnum()
#-------------------------------------------------------------------------------------------------------------------------------------------------
# def newdecor(sd):
#     def wrapper():
#         a=sd()
#         a+=10
#         return(a)
#     return wrapper
# @newdecor
# def s():
#     j=5
#     k=2
#     return j+k
# print(s())
#------------------------------------------------------------------------
#in below line use python debugger to understand it better
# ---------------------------------------------------------------------- 
# def add(f):
#     def wrapper():
#         a=f()
#         a+=10
#         return a
#     return wrapper
# def multi(f_):
#     def wrapper():
#         b=f_()
#         b*=10
#         return b
#     return wrapper
# def verynewff():
#     return 3
# kl=multi(add(verynewff))
# print(kl())
#------------------------------------------------------------------------
# def add(f):
#     def wrapper():
#         a=f()
#         a+=10
#         return a
#     return wrapper
# def multi(f_):
#     def wrapper():
#         b=f_()
#         b*=10
#         return b
#     return wrapper
# @multi
# @add
# def verynewff():
#     return 3
# print(verynewff())
#------------------------------------------------------------------------
# def decore32(add):
#     def wrapper(*args,**kwargs):
#         for i in args:
#             print(i)
#         return add(*args,**kwargs)
#     return wrapper

# def add(a,b):
#     s=a+b
#     return(s)
# w=decore32(add)
# print(w(2,4))
#########################################################################
#the above two line is also written bt syntatic sugar
#########################################################################
# def decore32(add):
#     def wrapper(*args,**kwargs):
#         for i in args:
#             print(i)
#         return add(*args,**kwargs)
#     return wrapper
# @decore32
# def add(a,b):
#     s=a+b
#     return(s)
# print(add(2,4))
#------------------------------------------------------------------------
#here ther is one more problem our actual add function is doing work on int data type but user can enter any data type , so to only allow ,int data type to our wrapper function and add function we import wraps from functool.
#------------------------------------END---------------------------------