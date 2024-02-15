s1 = { 11,22,33,44, }
print(s1)
print(type(s1))


s2 = {"Ajay",6,"Jawade",7}
print(s2)
print(type(s2))

s3 = {"Ajay"}
print(s3)
print(type(s3))

s4 = {}
print(type(s4))

s5 = ()
print(type(s5))

s6 = (6)
print(type(s6))


# Methods of SETS

a1 = {11,22,33,44,55,66}
print(a1)

print(22 in a1)

print(len(a1))

a1.add(99)
print(a1)

a1.add("Nita")
print(a1)

# for x in range(len(a1)):
#     print(x)

# print(a1[0])

a1.remove(55)
print(a1)

a1.pop()
print(a1)

# a1.clear()
# print(a1)

a1.update(["Ajay",22])
print(a1)

a1.update({65,78,"Aju"})
print(a1)

# set = a1
# set.remove("Ajay")
# print(set)
# print(a1)

a2 = a1.copy()
print(a2)

a2.remove("Ajay")

print(a1)
print(a2)

q1 = a1.union(s2)
print(q1)

setH = {11,22,33}
setJ = {44,55,66}
setK  = setH.union(setJ)
print(setK)

setL = {11,22,33}
setB = {44,55,33}
setQ  = setL.intersection(setB)
print(setQ)


q2 = a1.intersection(s2)
print(q2)
