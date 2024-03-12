def additon(x,y):
    return x+ y

q1 = additon(9,8)
print(q1)

def sub(x,y):
    return x- y

q2 = sub(y=11,x=23)    # Positional Argument

print(q2)

def mul(x=3,y=6):      # Default Argument
    return x * y

q3 = mul()
print(q3)
q4 = mul(3,5)
print(q4)



def addall(*args):     # Variable Length Arguments
    print(args)
    
addall(1,2,3,45,6,7,88,99)

def addAll(*args):
    total = 0
    for i in args:
         total = total + i
    return total

q3 = addAll(1,2,45,6,67,7,44,66)

print(q3)

from functools import reduce
def addAlll(*args):
    a = reduce(lambda acc,el:acc+el,args)      #Using REDUCE #Value of ACC not working
    return a
q3 = addAll(1,2,45,6,67,7,44,66)

print(q3)
 
def listA(*args):
    for x in args:
        print("Welcome "+ x)

listA("Nagpur","Pune","Chandrapur","Wardha") # Returning None




def listB(*args):
    b = list(map(lambda x:"Welcome "+x,args))
    return b

output = listB("Ajay","Tony","Raju","Amruta")

print(output)


def listC(*args):
    c = list(filter(lambda x : x > 40,args))
    return c

output2 = listC(45,67,32,1,2,3,11,22,4,33,44,55,45)
print(output2)

def dictA(**kwargs):
    print(kwargs)
    
dictA(firstName="Ajay",lastName="Jawade",age=20)


def dictA(**kwargs):
    for x in kwargs:
        print(x,kwargs[x])
    
dictA(firstName="Ajay",lastName="Jawade",age=20)




