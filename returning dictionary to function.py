def show(d):
    print(d)
    print(type(d))
    for i in d:
        print(i,"=",d[i])
    return d
dc={101:"rahul", 102:"raj",103:"surya"}
new_dc=show(dc)
print("****")
print(new_dc)
print(type(new_dc))