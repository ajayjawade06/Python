# A single try block can be follwed by several except block 
# Multiple except blocks can be used to handle multiple excpetions 
# We cannot write except block with try block
# We cannot write try block with except block
# Else block and finally block are not compulsory
# When there is no exception raised else block is executed after try block 
# Finally block is always executed

# Program 1

try : 
    names = ["Sarika","Poorva","Shraddha"]
    a = int(input("Enter a NumberA : "))
    b = int(input("Enter a NumberB : "))
    print(a/b)
    
except ArithmeticError : 
    print("Please Enter Correct Input ")
    
except IndexError : 
    print("Please add more values to list")
    
# Program 2

print("Ajay")

try: 
    print(34/0)
    
finally:
    print("I will always execute")
    
print("Bye")

# Program 3

def calAvg(list):
    [11,22,33][4]
    total = 0 
    for item in list:
        total = total + item
    avg = total/len(list)
    return total,avg

try:
    a,b = calAvg([1,2,3,"a"])
    print(a)
    print(b)
except TypeError:
    print("Enter the correct input")
except ZeroDivisionError:
    print("Enter Correct Input")
    
print("Hello")
try:
    x=18
    assert x > 1 and x < 9
except AssertionError:
    print("Condition Not Matched")
    
class lowBalance(Exception):
    def __init__(self,msg):
        self.msg = msg
        
def check(dict):
    for k,v in dict.items():
        if(v<20000):
            raise lowBalance("Balance is Low")

try:
    names = {"Snehal" : 100000,"Ajay" : 400000,"Chinmay" : 500000,"Tony" :4000000}
    check(names)
    print(names)

except lowBalance as msg:
    print(msg)
    






