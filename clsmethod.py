# class Person:
#     country = "India"
#     def __init__(self,fn,ln,rollNo,age):
#         self.firstName = fn
#         self.lastName = ln
#         self.rollNo = rollNo
#         self.age = age
        
#     def displayName(self):
#         print(self.firstName + self.lastName)
        
#     def updateAge(self,ag):
#         self.age = ag
        
# ajay = Person("Ajay","Jawade",12,20)

# ajay.displayName()


# ajay.country = "Bharat"

# print(ajay.country)

# ajay.updateAge(21)

# print(ajay.age)



# Program 2

# class Person:
#     country = 'India'
#     def __init__(self,fn,ln,age):
#         self.firstName = fn
#         self.lastName = ln
#         self.age = age
        
#     @classmethod
#     def updateCountry(cls,country):
#         cls.country = country
        
#     def updateAge(self,age):
#         self.age = age
        
# ajay1 = Person("Ajay1","Jawade1",20)
# ajay2 = Person("Ajay2","Jawade2",20)
# ajay3 = Person("Ajay3","Jawade3",20)

# print(ajay1.country)
# print(ajay2.country)
# print(ajay3.country)

# Person.country = "Bharat"

# print(ajay1.country)
# print(ajay2.country)
# print(ajay3.country)

# Program 3
# Count of Object

class vehicle:
    count = 0
    country = "India"
    def __init__(self,color,type):
        self.color = color
        self.type = type
        vehicle.count = vehicle.count +1
        
    def updateColor(self,cl):
        self.color = cl
        
    @classmethod
    def updateCountry(self,con):
        self.country = con
        
    @staticmethod
    def countobj():
        print(vehicle.count)
        
audi = vehicle("blue","sedane")
bmw = vehicle("red","suv")
maruti = vehicle("green","jeep")
bmw2 = vehicle("red","suv")       

print(audi.country)
print(bmw.country)
print(maruti.country)

vehicle.country = "Bharat"
print(audi.country)
print(bmw.country)
print(maruti.country)

vehicle.countobj()




        
