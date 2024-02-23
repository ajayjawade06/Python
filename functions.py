# Function

# int as parameter and int as return

def add(x,y):
    return x+y

e = add(12,3)
print(e)
print(type(e))

# float as parameter and float as return

def add(x,y):
    return x+y

f = add(34.5,7.8)
print(f)
print(type(f))

# string as parameter and string as return type

def greet(word):
    return "Hello "+word

g = greet("Aju")
print(g)
print(type(g))

# list as parameter and list as return type]

city = ["pune","nagpur","chandrapur","rajura"]

def citi(lst):
    city.append("wardha")
    return lst

h = citi(city)
print(h)
print(type(h))

# Dict as parameter and Dict as return type

info = {
    "firstname" : "Ajay",
    "lastname"  : "Jawade"
}

def dict(dict):
    info["age"] = 21
    return dict
      
i = dict(info)
print(i)
print(type(i))

# Tuple as parameter and tuple as return type

a1 = 12,13
a2 = (12,13)

print(a1)
print(type(a2))

def addElementToTuple(tupA):
    tupA = list(tupA)
    print(tupA)
    tupA.append(34)
    tupA = tuple(tupA)
    return tupA

j = addElementToTuple(a1)
print(j)
print(type(j))

# set as parameter and set as return type

setA = {11,22,33}

def addEtoS(x):
    setA.add(x)
    return setA

k = addEtoS(23)
print(k)
print(type(k))













