# set1 ={11,23,33,44,55,6}
# print(set1)
# set1.discard(44)
# print(set1)
# set1.remove(23)
# print(set1)

# set1.pop()
# print(set1)

# set1.add(90)
# print(set1)

# set1.update({178,77,65})
# print(set1)

# set1.update([22,33,445])
# print(set1)

# set2 ={11,445,22,33,9}
# print(set1)
# print(set2)
# diff =set1.difference(set2)
# print(diff)

# union = set2.union(set1)
# print(union)


set3 = {11,22,33,44,55,100}
set4 = {11,22,33,44,55,90}

union = set3.union(set4)

print(union)

set6 =set3.symmetric_difference(set4)
print(set6)

print(set3.symmetric_difference(set4))

print(set3.isdisjoint(set4))

print(set3.issubset(set4))

print(set3.issuperset(set4))

inter = set3.intersection(set4)
print(inter)

print(set3.intersection_update(set4))

print(set3.isdisjoint(set4))

