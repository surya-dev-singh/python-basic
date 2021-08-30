#higher order function 
# when we pass a function inside a funtion , then it is called higher order function.
# in python we have three main higher order function
#---filter() function: 
#The filter function is used to filter out the elements of an iterable(sequence) depending on a function that tests each elements in the sequence to be true or not.
#it returns those elements of squence, for which function is true
#syntax:
#filter(function_name,itreable)
#function_name : its's name of a function which tests each elements in the sequence return True or False.if function is None , returns the elementd that are true.
#iterable: iterable may be either a sequence , list , string , tuple , a container which supports iteration , or an iterator.
#------------------------------------------------------------------------
a=[10,50,60,80,90,5,45,65]
def high_marks(n):
    if n>=60:
        return True
result=filter(high_marks,a)
print(result)
print(type(result))
#fiter function will always return a filter object, which is iterable. we can also convert filter object to list using list() function.
#other way to use filter function for handy purpose:
b=[1,2,3,4,5,6,7,8,9,10]
for i in filter(lambda x:(x>=5),b):print(i)
#there is always differnt location in memory created for every lamda function.
#other use
c=[True,False,True,True,False,False,True]
for i in filter(None,c):print(i)
#----------------------------------END-----------------------------------