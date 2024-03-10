

class Person:
    
    country = "INDIA"
    def __init__(self,fn,ln,age,salary):
        self.firstName = fn
        self.lastName = ln
        self.age = age
        self.salary = salary
        
    def display(self):
        print("Name :",self.firstName + " " + self.lastName,"\nAge :",self.age,"\nSalary :",self.salary,"\nCountry :",self.country)
                
    def updateAge(self,age):
        self.age = age
        
    def updateSalary(self,sl):
        self.salary = sl
        
ajay = Person("Ajay","Jawade",20,1000)

ajay.display()
ajay.updateAge(21)
ajay.display()
ajay.updateSalary(20000)
ajay.display()


tony = Person("Tony","Stark",36,10000000)

tony.display()
tony.country = "USA"

tony.display()
ajay.display()








