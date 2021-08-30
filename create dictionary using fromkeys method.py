#This method is used to create a new dictionary with specified keys and values.
#we can not give multiple value while defining the dictionary uding fromkeys method.

key=(101,102,103)
value="surya"
d=dict.fromkeys(key,value)
print(d)

k=(1,2,3)
v="a"
e=dict.fromkeys(k)
print(e)

k1=(101,102,103)
v1=("a","b","c")
# if we give mutiple value and define our dictionary uding fromkeys method.this will set that values to all keys.
f=dict.fromkeys(k1,v1)
print(f)

a={}
mykeys=(1,2,3)
myvalue="surya"
b=a.fromkeys(mykeys,myvalue)
print(b)
