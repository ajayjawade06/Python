info = {
    "fisrtName" : "Ajay",
    "lastName"  : "Jawade",
    "age"       : 20,
    "Class"     : "BCA",
    "age"       : 18    
}

#retrive
print(info)

#update
info['Class'] = "BCA 3rd Year"

print(info)

#add

info["city"] = "Nagpur"

print(info)

#delete

info.pop("lastName")
print(info)

print("Class" in info)

print(info["age"])


vehicle = {
    "type"  : "SUV",
    "color" : "black"
}
print(vehicle)


for item in vehicle:
    print(item)
for item in vehicle:
    print (item,vehicle[item])
    
print(type(vehicle))

print(len(vehicle))
print(len(info))
    
student = {
    "firstName":"chinmay",
    "lastName":"deshpande",
    "age":34,
    "rollNo":55
}

for key in student:
    print(key)
    
for val in student:
    print(val,student[val])


animal = {
    "color":"red",
    "legs":4,
    "name":"tiger"
}

for key in animal:
    print(key,animal[key])
    
    # Keys() method 
    
print(animal.keys())
print(animal.values())

for key in animal.keys():
    print(key)

for val in animal.values():
    print(val)
    
    
    # item()
for k,v in animal.items():
    print(k,v)
    
subjects = {
    "subOne":"marathi",
    "subTwo":"hindi",
    "subThree":"english",
    "subFour":"sanskrit"
}

# keys(),values(),items()

for key in subjects.keys():
    print(key)
    
for val in subjects.values():
    print(val)
    
for k in subjects.items():
    print(k)

#subjects.clear()
#print(subjects)

#pop

subjects.pop("subOne")
print(subjects)

subjects.popitem()
print(subjects)

subjects2 = {
    "subOne":"geography",
    "subTwo":"history",
    "subThree":"science",
    "subFour":"Maths"
}

subjects3 = subjects2
#subjects2["subFour"] = "Civics"
#print(subjects2)
#print(subjects3)

subjects3 = subjects2.copy()
print(subjects3)



students ={
    "first_name" : "Ajay",
    "last_name"  : "Jawade"
}
print('Hello')
print(students.get("first_name"))
print('bye')

a = students.get("first_nam")
b = students["first_name"]

print(a)
print(b)

