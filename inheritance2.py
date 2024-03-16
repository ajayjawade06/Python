# Single Inheritance

class students:
    def __init__(self,fn,ln):
        self.firstName = fn
        self.lastName = ln
        
    def displayName(self):
        print(self.firstName + " " + self.lastName)
        
class teacher(students):
    def __init__(self, fn, ln,salary):
        super().__init__(fn, ln)
        self.salary = salary
        
    def displaySalary(self):
        print(self.salary)
        
ajay = teacher("Ajay","Jawade",100000)

ajay.displayName()
ajay.displaySalary()
