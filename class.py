# class person:
#     firstName = "Ajay"
#     lastName = "Jawade"
#     age = 20
    
#     def display(self):
#         return(self.firstName + " " + self.lastName)
    
# ajay = person()


# print(ajay.firstName)
# print(ajay.lastName)
# print(ajay.age)
# print(ajay.display())

# tony = person()

# tony.firstName = "Tony"

# tony.city = "Pune"

# print(tony.firstName)
# print(tony.lastName)
# print(tony.age)
# print(tony.city)
# print(tony.display())

# Program 2

class Person : 
    def __init__(self,fn,ln,age):
        self.firstName = fn
        self.lastName = ln
        self.age = age
        
    def display(self):
            print(self.firstName + " " + self.lastName)
        
    def displayAge(self):
            print(self.age)
        
aju = Person("Ajay","Jawade",21)

raj = Person("Raj","Bawane",22)

aditya = Person("Aditya","Jawade",16)

aju.display()
aju.displayAge()
raj.display()
raj.displayAge()

print(aju.firstName)

students =[aju,raj,aditya]

for x in students:
    x.display()
    x.displayAge()
    
# Program 3

class vehicle:
    def __init__(self,color,type):
        self.color = color
        self.type = type
        
    def displayColor(self):
        print(self.color)
        
        
audi = vehicle("red","sedane")
bmw = vehicle("black","suv")
        
audi.displayColor()
bmw.displayColor()





