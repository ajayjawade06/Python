def addA(x,y):
    print(x+y)
    
addA(12,3)

# default arguments

def addA(x=7,y=3):
    print(x+y)
    
addA()
addA(3,4)

# Positional Arguments

def addC(x,y):
    print(x - y)
    
addC(y=10,x=11)



def addD(*args):
    print(args)
    total = 0
    for x in args:
        total = total + x
    return total

e3 = addD(1,2,3,4,5,6,7,8,9)
print(e3)



def addinfo(**kwargs):
    print(kwargs)
    kwargs['city'] = "chandrapur"
    return kwargs
e4 = addinfo(first_name = "ajay",last_name ="jawade",age= 20)
print(e4)



def function():
    a=1
    b=2
    a = a+1
    print(a)
    print(b)
    
function()

x = 1
def myfunc():
    y = 4
    x = 6
    x = x+1
    print(x)
    print(y)
    
myfunc()
print(x)

a =10
def myfunnction():
    print(a)
    print(10)
    
myfunnction()
print(a)

h =10

def myfunction1():
    global h
    h=99
    print(h)
    
myfunction1()
print(h)


    