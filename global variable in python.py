#when a variable is declared above a function , it become global variable. these variable are available to all the function which are written after it. the scope of global variable is the entire program body written below it.
a=50
def show():
    x=10
    print(x)
    print(a)
show()
print("global variable:",a)
#------------------------------------------------------------------------if global variable and local variable name are same,and we do not writw local variable , then it will generate error,ofr eg:-
# i=0
# def myfun():
    # i=i+1#here the second i which is in expression , should be a defined local variable
    # print(f"my function{i}")
# myfun()
#------------------------------------------------------------------------
# j=9
# def new():
    # j=7
    # j=j+1#here it is using local variable, be we supposed it that it would use global variable
    # print(j)
# new()
#------------------------------------------------------------------------
# so, to overcome this problem we use global keyword!
#---------------------------------END------------------------------------