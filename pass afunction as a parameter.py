# we can pass a function as a parameter to another function.
def disp(sh):
    print("disp function "+ sh())
def show():
    return "show function"
disp(show)
# ----------------------------END-----------------------------------------