#set methods

a={"rahul","raj","sonam","surya"}
b={"sumit","rahul","surya","python","java"}

print("A = ",a)
print("A = ",b)
print()

#intersection method
ism=a.intersection(b)
print(ism)

#union method
unm=a.union(b)
print(unm)

#difference
diff1=a.difference(b)
print(diff1)
diff2=b.difference(a)
print(diff2)

#is subset
# this return true if all items of the set exists in the specified set.
i=a.issubset(b)
print(i)

#is supperset
#this returns true if all items of specified set exist in original set
s=a.issuperset(b)
print(s)

#there are more methods like difference_update and  intersection_update
# we we do not use it frequently .
 