# list Comprehension
# list Commprehension

# [expression : loop : condition]

# table of 2 

x = [1,2,3,4,5,6,7,8,9]

out = [i *2 for i in x]
print(out)

# Even Number

out2 = [i for i in x if i % 2 == 0]
print(out2)

# Odd Number

out3 = [i for i in x if i % 2 != 0]
print(out3)

# Make every char to UPPER

names = ["ajay","sarika","chinmay","poorva"]
out3 = [i.upper() for i in names ]
print(out3)

out4 = [i.upper() for i in names if i.endswith('y') ]
print(out4)

out5 = [i[0] for i in names]
print(out5)


listofDict = [{
    
    "firstName" : "Ajay",
    "lastName"  : "Jawade",
    "age"       : 20,
    "vehicle"   : True
},
{
    "firstName" : "Tejas",
    "lastName"  : "Jawade",
    "age"       : 16,
    "vehicle"   : True  
},
{
    "firstName" : "Aditya",
    "lastName"  : "Jawade",
    "age"       : 13,
    "vehicle"   : False
}]

firstname = [x["firstName"] for x in listofDict ]
print(firstname)

nums = [11,22,33,44]
# [odd,even,odd,even]

out6 = ["Even" if x%2 == 0 else "Odd" for x  in nums]
print(out6)

out7 = [x["firstName"] for x in listofDict if x["age"]>18 and x["vehicle"]== True]

print(out7)

out8 = [i['firstName'] if i['age']>18 and i['vehicle']==True else None for i in listofDict ]
print(out8)

out8 = [i['firstName'] if i['age']>18 and i['vehicle']==True else None for i in listofDict ]
print(out8)

out9 = [x for x in out8 if x != None]
print(out9)

# Can Drive Cannot Drive

out10 = [i["firstName"]+ " : "+ ("Can Drive " if i["age"]>18 and i['vehicle']==True else  "Cannot Drive") for i in listofDict ]
print(out10)




