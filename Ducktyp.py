# # Duck Typing

# class Duck : 
#     def talk(self):
#         print("quack quack")
        
# class Human:
#     def talk(self):
#         print("hi hello")
        
# def call_talk(obj):
#     obj.talk()


# duckA = Duck()

# amol = Human()

# call_talk(duckA)
# call_talk(amol)

class Duck():
    def talk(self):
        print("quack quack")
        
class Dog():
    def bark(self):
        print("bhow bhow")
        
def call_talk(obj):
    if hasattr(obj,'talk'):
        obj.talk()
    else:
        obj.bark()
        

duckA = Duck()
tommy = Dog()

call_talk(duckA)
call_talk(tommy)


# Operator Overloading

print(1+1)

print("hello " + "world")

class BookX:
    def __init__(self,pages):
        self.pages = pages
        
    def __add__(self,obj):
        return self.pages +  obj.pages  
    
    
class BookY:
    def __init__(self,pages ):
        self.pages = pages
        
    def __add__(self,obj):
        return self.pages + obj.pages
        
ramayan = BookX(100)
mahabharat = BookY(200)

print(ramayan.pages + mahabharat.pages)

print(ramayan + mahabharat)
print(mahabharat + ramayan)






