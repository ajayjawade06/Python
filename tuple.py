info = {
    "first_name" : "Ajay",
    "last_name"  : "Jawade",
    "age"        : 20
}

# info.update({"class":"BCA"})
# print(info)

#info.clear()
#print(info)

#info.pop("last_name")
#print(info)

#info.get("first_name")
#print(info)

#info2 =info.copy()
#print(info2)

#info.popitem()
#print(info)

#keys = info.keys()
#print(keys)

#values = info.values()
#print(values)

#items = info.items()
#print(items)

# e1 = dict.fromkeys(["Tony","Ajay","Amol"])
# print(e1)


# info.setdefault("occupation","Student")
# print(info)



###########################################################################################################################

tuple = (11,22,33,44,33,22,44,66) #Tuples are declared using parenthesis()

print(tuple)

# Methods

a1 = tuple.count(22)
print(a1)

a2 = tuple.index(44)
print(a2)

# Printing Tuple using range

for x in range(len(tuple)):
    print(x)         # Print Index of Tuple     
    print(tuple[x])  # Print Elements of Tuple
    
# Printing Tuples without Range

for items in tuple:
    print(items)
    
