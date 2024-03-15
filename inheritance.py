# program 
# Single Inheritance
class student():
    def __init__(self,fn,ln,aadhar):   
        
        self.firstName = fn
        self.lastName = ln
        self.aadhar = aadhar      
        
    def display(self):
        print(self.firstName + " " + self.lastName)

# ajay = student("Ajay","Jawade") 

# ajay.display()

class teacher(student):
    def __init__(self, fn, ln, aadhar,salary):
        super().__init__(fn, ln, aadhar)
        self.salary = salary
        
    def displaysalary(self):
        print(self.salary)
        
ajay = teacher("Ajay","Jawade",329566342551,20000)




print(ajay.firstName)
print(ajay.lastName)
print(ajay.aadhar)
print(ajay.salary)

ajay.display()
ajay.displaysalary()



# Multiple Inheritance

class grandfather:
    def __init__(self,fn,ln):
        self.firstName = fn
        self.lastName =ln
        
    def displayGname(self):
        print(self.firstName + " " + self.lastName)  
        
class father(grandfather):
    def __init__(self, fn, ln,fname):
        super().__init__(fn, ln)
        self.fname = fname
        
    def displayFname(self):
        print(self.fname + " " + self.lastName)

class son(father):
    def __init__(self, fn, ln, fname,sname):
        super().__init__(fn, ln, fname)
        self.sname = sname
        
    def displaySname(self):
        print(self.sname + " " + self.lastName)
        
ajay = son("Ramuji","Jawade","Latari","Ajay")

ajay.displayGname()
ajay.displayFname()
ajay.displaySname()
    






