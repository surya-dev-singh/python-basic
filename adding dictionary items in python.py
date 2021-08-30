# we can add an item to dictionary just by mentioning a new key-valu pair into an existing dictionary.  

#if we mention a key which is already exists in the dictionary then the value gets updated/modified rather then adding a new item.

# the new item may be added at any place in the dictionary as dictionary is an unorderd collection.

# the value need not to be unique, key should be unique, in case if the key is  not unique  then its value get updated in dictionary rather than adding a new item.

stu={
    101:"rahul",
    102:"raj",
    103:"arpit"
}
print("before adding :")
print(stu)
print(id(stu))
print()

stu[104]="surya"
print("after adding")
print(stu)
print(id(stu))
print()
