# Program 1

def addition(fn,x,y):
    fn = lambda x,y:x+y
    e = fn(x,y)
    
    return e

add = lambda x,y:x+y
result = addition(add,12,4)

print(result)

def dmas(fn,x,y):    
    res = fn(x,y)
    return res

d = lambda x,y:[x+y,x-y,x*y,x/y,x%y]

result = dmas(d,12,4)

print(result)
print(type(result))

# program 2
# function as a parameter to another function

sub = lambda x,y:x-y

def substraction(fn,a,b):
    e = fn(a,b)
    return e

minus = substraction(sub,8,6)

print(minus) 

# Program 3
# function as a return type

def multiplication():
    return lambda x,y:x*y


mul = multiplication()

multiply = mul(4,8)

print(multiply)

# Program 4 

def modulas():
    return lambda x,y:x%y

mod = modulas()

ress = mod(12,4)
print(ress)






