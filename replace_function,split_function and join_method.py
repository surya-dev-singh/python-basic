#--- replace()method---
    #this method is is used to replace a sub string in a string with another sub string .
    #syntax:- string.replace(old,new)
#---split()method---
    #this method is used to split/break a string into pices .these peices return a list.
    #syntax:-string.split("seperator")
#---join()method---
    #this method is used to join string into one string
    #stntax:-"seperator".join(string_list/tuple)
#------------------------------------------------------------------------
name="geekyshows"
print(name.replace("geeky","rahul"))
#------------------------------------------------------------------------
name1="hello_how_are_you"
print(name1.split("_"))
#------------------------------------------------------------------------
name2=('hello','how','are','you')
print('_'.join(name2))
name3=['i','am','fine']
print('-'.join(name3))
#----------------------------------END-----------------------------------
