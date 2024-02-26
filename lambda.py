def add(x,y):
    return x + y

e = add(12,4)

print(e)

addB = lambda x,y:x+y

e2 = add(34,7)

print(e2)

e = lambda x,y:x*y
addC = e(3,4)
print(addC)

q = lambda x:x*x
addD = q(78)
print(addD)

names = ["Amit","Akay","Shivani"]
def changeName(lst):
    lst[0] = "Ajay"
    return lst

print(names)

a4 = changeName(names)
print(a4)


city = ["pune","nagpur",'kolkata']
city2 = city

city[1] = "chandrapur"

print(city)
print(city2)


listA = [1,2,3,4,5]

n = []

for i in listA:
    n.append(i*5)
    
print(n)

# List Comprehension
# [expression : loop : condition]

q1 = [i*5 for i in listA]
print(q1)

listB = [1,2,3,4,5,6,7,8,9,10]

q2 = [x*x for x in listB]
print(q2)

listC = [44,55,66,77,88,99,11,22,33,44,55,7,8,9]

listD = []

for x in listC:
    if x%2 == 0:
        listD.append(x)
        
print(listD)

z = [x for x in listC if x%2==0]

print(z)

