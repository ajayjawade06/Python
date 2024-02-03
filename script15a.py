info = {
    "first_name" : "Ajay",
    "last_name"  : "Jawade",
    "age"        : 20,
    "class"      : "BCA "
       
}

#RETRIVE

print(info)

#UPDATE

info["class"] = "BCA 3rd Year"

#ADD

info["blood_group"] = "O+"
print(info)

#DELETE

info.pop("last_name")
print(info)

info.popitem()
print(info)

a = info.values()
print(a)

b = info.keys()
print(b)


