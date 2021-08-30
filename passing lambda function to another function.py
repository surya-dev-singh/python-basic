#we can pass lambda function to another function
#------------------------------------------------------------------------
def show(a):#here a has become function variable , because passing lambda
    print(a(8))
show(lambda x:x**2)
#---------------------------END------------------------------------------