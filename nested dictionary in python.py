# A dictionary inside another dictionary is called as nested dictionary or nesting of a dictionary.

#creating empty nested dictionary:
a={
    1:{},
    2:{},
    3:{},
    4:{}
}

#creating and accesing nested dictionary
a={"course":"python",
    "fees":1500,
    1:{"course":"javascript","fees":10000}
    }
print(a["course"])
print(a["fees"])
print(a[1])
print(a[1]["course"])
#updating:
print()
a["duration"]="6 months"
print(a)

a.pop("duration")
print("**************************************************")

#accesing nested dictionary using for loop:
for i in a:
    if type(a[i]) is dict:
        for k in a[i]:
            print(k,"=",a[i][k])
    else:
        print(i,"=",a[i])

print("****************************************************")
#another type of nested dictionary:
a={
    1:{"course":"python","fees":15000},
    2:{"course":"javascript","fees":10000}
}
print(a[1])
print(a[2])
print()
print(a[1]["course"])
print(a[2]["fees"])
#updating dict:
a[1]["course"]="machine learning"
print(a)

#deleting item in dict:
del a[1]["course"]
print()
print(a)

a[1]["course"]="python"

print("**************************************************")
#accessing the above dictionary using for loop:

for i in a:
    for k in a[i]:
        print(k,"=",a[i][k])
