nums = [1,2,3,4,5]

print(nums)

# MAP

e = lambda x : x + 5

plus5 = e(10)
print(plus5)

e = lambda x : x + 5

e2 = list(map(e,nums))
print(e2)


numbers = [11,44,55,66,77,33,44]
mapfn = list(map(lambda x : x + 5,numbers))

print(mapfn)

names = ["Ajay","Aditya","Tejas"]

fullName = list(map(lambda x : x + " Jawade",names))

print(fullName)


# FILTER

transactions = [55,-66,33,-44,55,-66,80]

for x in transactions:
    if x > 0:
        print(x)

for x in transactions:
    if x < 0:
        print(x)
        
deposit  = [x for  x in transactions if x > 0 ]
print(deposit)

withdrawal = [x for x in transactions if x < 0]
print(withdrawal)

e3 =  list(filter(lambda x : x > 0,transactions))
print(e3)

e4 = list(filter(lambda x : x < 0,transactions))
print(e4)

marks = [20,3,49,50,59,60,39,69,50]

e5 = list(filter(lambda x : x > 50,marks))
print(e5)

# REDUCE

from functools import reduce

listA = [11,22,33]

e6 = reduce(lambda acc,el : acc+el,listA,0)
print(e6)


listb = [9,2,3,495,6,65,595,0]

e7 = reduce(lambda acc,el:acc+el,listb,0)
print(e7)



