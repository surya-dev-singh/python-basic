# what is comprehension:
# Comprehension contains very compacr code usually a single startement that perform a task.
# This are of three types:
#1.list comprehension
#2.set comprehension
#3.dictionary comprehension

#LIST COMPREHENSION:

#list comprehension represent creation of new list from an iterables object that satisfy a given condition.

#syntax:

#new_list=[expression for item in iterable_object if_statement]

#There can be zero or more If statements.
#There can be one or multiple for loops.
#------------------------------------------------------------

#creating list without list comprehension:

list1=list(range(20))
new_list=[]
for i in list1:
    new_list.append(i**3)
print(new_list)

#creating list with list comprehension:
print("****************************")
print([i**3 for i in list1])

#using list comprehension with if statement:
print("****************************")
print([i**2 for i in range(10) if i%2==0])
print([i**2 for i in range(10) if i%2==0 if i%3==0])

#list comprehension with if else statement:
#syntax:
#new_list=[expresion if_stement else expresion for item in iterable_object]
print()
print([i if i%2==0 else "invalid" for i in range(10)])

#nested list comprehension:
print("*********************")
print([[i*j for j in range(4,7)] for i in range(6,8)])


