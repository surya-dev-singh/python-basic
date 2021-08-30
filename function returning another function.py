# a function can return another function , we called it as closure, or first class function.
def disp():
    def show():
        return"show function"
    print("disp function")
    return show
r_sh=disp()
print(r_sh())
##
def disp(sh):
    print("disp function")
    return sh
def show():
    return"show function"
r_sh=disp(show)
print(r_sh())
#--------------------------END-------------------------------------------
