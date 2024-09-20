#dict:
flist={
    "a":"apple",
    "b":"banana",
    "c":"cherry",
    "d":"date",
    "e":"elderberry", 
}
print(type(flist))
print(flist)

print(flist["a"])
print(flist["b"])
print(flist["c"])
print("by using for loop:")
for  key in flist:
    print(key,":",flist[key])
    
'''mydict={
    "name":"jayraj",
    "age":25,
    "city":"Nwe york",
}
print(mydict)
mydict.update({
    "country":"USE",
    "phone":"1234567890"
})
print(mydict)

print("conName:",mydict.get("country"))

print("keys:",mydict.keys())
print("values:",mydict.values())
print("Items:",mydict.items())
#ex.3
mydict={
    "name":"jayraj",
    "age":25,
    "city":"Nwe york",
}
print(mydict["name"])
mydict['name']="sanket"
print(mydict["name"])
print(mydict)

del mydict["age"]
print(mydict)
dict_length=len(mydict)
print(dict_length)
'''