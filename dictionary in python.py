#A dictionary repesents a group of elements in the form of key values pairs. 
#dictionary in python is an unorder collection
#dictionary are mutable so, we can modify it's identity , withour changing their identity.
#dictionary are presented using { }


#creating an empty dictionary.
fees={}

#creating a dictionary:

# a dictionary is created in the form of key-value pair where keys can't be repeated and must be immutables and values can be of any datatype and be duplicate.
#keys are case sensitive
stu={101:"rahul",102:"raj",103:"surya"}
print(type(stu))
fees={
        "rahul":2000,
        "raj":3000,
        "surya":4000
        }

#keys rule:
# 1.key should be unique
# 2.if we mention same key again , the old key will be overwritten
#keys should be immutable objects type like :- int, string , tuple
#we can not use list or dictionary as key

#accessing dictionary:
#we can access the value of a dictionary by reffering to its key name, inside square brackets.

print(stu[101])
print(stu[102])
print(fees["rahul"])

