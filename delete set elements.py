# we can delete elements using remove() or discard() method.
#remove() mehtod rais error if elements doesn't exits, while discard() mehtod remains unchanged.

a={10,20,"surya",40}
print("original set",a)
print(id(a))
print()

a.remove("surya")
# a.remove("adasd") #this will give u error brcause the specified element is not in out set
print("after removing set",a)
print(id(a))
print()

a.discard("af") #this will not generate error , even if the specified elements is not our set.
print(a)

del a