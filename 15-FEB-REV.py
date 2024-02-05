'''for x in range(5):
    print(x)

for x in range(2,4):
    print(x)'''

#list1 = ["Ajay","Tony","Piyush","Komal"]

#list.sort()
#print(list)

#list.reverse()
#print(list)

''' list1.extend(["Aju","Kajal"])
print(list1)

list1.remove("Aju")
print(list1)

list1.append("Sham")
print(list1)

list1.pop()  
print(list1)

list1.insert(2,"Chanchal")
print(list1)

list2 = list1.copy()

q1 =list2.count("Ajay")
print(q1)

s1 =list1.index("Piyush")
print(s1) '''
        #  0       1       2       3     4
'''names = ['amol','ajay','sarika','amit','raj']
#         -5     -4      -3      -2     -1
print(names)

for x in names:
    print(x)
    
for x in range(len(names)):
    print(names[x])
print(names[4:len(names):])
print(names[-3:len(names):])
print(names[-1:-10:-2])
print(names[1:3:1])
'''
'''name = ['ajay','tony','raju']

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
'''

info = {
    "firstName" : "Ajay",
    "lastName"  : "Jawade",
    "age"       : 21,
    "class"     : "BCA"
}
'''
#RETRIVE

print(info)

#UPDATE

info["class"] = "BCA 3rd Year"

#ADD

info["bloodgroup"] = "O+"
print(info)

#DELETE

info.pop("lastName")
print(info)

info.popitem()
print(info)

for item in info:
    print(item)
    print(info[item])
    
info2=info
print(info2)

info["age"] = "20"

print(info)
print(info2)

for item in info:
    print(item, info[item]) '''
'''
#print(type(info))
#print(len(info))

animal ={
    "color" : "Black",
    "name"  : "Panther",
    "legs"  : 4
}

keys = animal.keys()

print(keys)

for keys in animal.keys():
    print(keys)

for values in animal.values():
    print(values)

for item in animal.items():
    print(item)'''

#for k,v in animal.items():
 #   print(k,v)
    
'''   
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
print(subjects3)'''

students ={
    "first_name" : "Ajay",
    "last_name"  : "Jawade"
}
print("Hello")
print("first_name")
print("bye")

a = students.get("first_nme")
b = students["first_name"]

print(a)
print(b)












