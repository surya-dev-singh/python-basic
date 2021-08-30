#---recursion in python ----
    # when a function call itself again and again to compute a value is referred to recursive function or recursion.
    #the default recursion limit in python is 1000
#------------------------------------------------------------------------
i=0
def myfun():
    global i
    i+=1
    print("suryadev",i)
    myfun()
myfun()
##uncomment the following line to se the result:
# i=0
# def mynum():
#     a=globals()['i']
#     a+=1
#     print("hello",a)
#     mynum()
# mynum()
# print(i)
#------------------------------------------------------------------------
#how to change/see recursion limit in python.
# import sys
# print(sys.getrecursionlimit())
# sys.setrecursionlimit(4000)
# print(sys.getrecursionlimit())
#-------------------------------END--------------------------------------