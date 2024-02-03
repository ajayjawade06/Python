'''
names = ['amol','ajay','sarika','amit','raj']
print(names)

for x in names:
    print(x)
    
for x in range(len(names)):
    print(names[x])
print(names[4:len(names):])
print(names[-3:len(names):])
print(names[-1:-10:-2])


names.append("kaju")
print(names)

a= names.extend(["aju",'vijay'])
print(names)
print(a)

a1 = names.sort()
print(names)
print(a1)

a2 = names.insert(0,"Appi")
print(names)
print(a2)

names.remove("kaju")
print(names)

names.pop()
print(names)

#a3 = names.clear()
#print(a3)
#print(names)

a1 = names.copy()
print(names)

a1.append("badam")
print(a1)

a5 =names.count("ajay")
print(a5)
print(names)

a6 = names.reverse()
print(a6)
print(names)
'''


cities = ["nagpur","kanpur",'solapur']
cities1 = cities.copy()
cities[0] = "pune"
print(cities)
print(cities1)










