#---nested function---
#when we define one function inside another function ,it is known as nested function or function nesting.
def disp():
    def show():
        print("show function")
    print("disp function")
    show()
disp()
#-----------------------------END---------------------------------------