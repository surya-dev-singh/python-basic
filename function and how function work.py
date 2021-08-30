#---functions()---
    #functions are dub programs which are used to compute a value or perform a task.
#---types of functions---
    #1.buitin function #eg:print(),upper()etc
    #2.user-defined function
#syntax:-
#def add(y):
#   x=10,y=10
#   c=x+y
#   print(c)
#add(20)
#here y is parameter and 20 is argument.
#in functions parameters does not know which type of data they will recive till the value is passed at the time of calling a function . this means the type of data is determined only during runtime not at the compile time, this is called dynamic typing.
#-----------------------------------------------------------------------
def disp():
    name="geekyshows"
    print("welcome to",name)
disp()
def add(y):
    x=10.233
    print(x+y)
    print(f"formatted output {x+y:.2f}")
add(20)
#----------------------------------END-----------------------------------


 
