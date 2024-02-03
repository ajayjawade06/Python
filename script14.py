name = ['ajay','tony','raju']

#retrive

print(name)

#update

name[2] = 'kaju'
print(name)

#add

name.append('bhalu')
print(name)

#delete

name.pop()
print(name)
name.remove('tony')
print(name)


# DICTIONARY    

info = {
    "firstName" : "Ajay",
    "lastName"  : "Jawade",
    "age"       :   20
    
}
#RETRIVE

print(info)

#ADD

info["address"] = "Upparwahi"

print(info)

#DELETE
info.pop("lastName")
print(info)

info.popitem()
print(info)

#UPDATE

info['firstName'] = "Tony"  
print(info)

#NEW DICTIONARY

vehicle = {
    "color" : "Red",
    "type"  : "SUV"
}

#retrive

print(vehicle)
print(vehicle['color'])

#update

vehicle["color"] = "black"
print(vehicle)

#add

vehicle['regNo'] = "MH 34 CA 0558"
print(vehicle)

#delete

vehicle.pop("color")
print(vehicle)
vehicle.popitem()
print(vehicle)


fruits = ['apple','mango','kiwi','apple','watermelon']

print(fruits)

info ={
    "name"     : "Ajay Jawade",
    "age"      : 20,
    "address"  : "Upparwahi",
    "age"      : 45
}

print(info)






