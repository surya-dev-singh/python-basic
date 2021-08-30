#---nested lambda function---
    #when we write lambda function inside another lambda function that is called nested lambda function.
#------------------------------------------------------------------------
add=lambda x=10:(lambda y: x+y)
a=add()#here add() is returning inner lambda function , so a has become function variable. we can check it by print(a)
print(a(5))
#--------------------------------END-------------------------------------
