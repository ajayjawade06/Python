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


# Multi-Level Inheritance

class grandFather:
    def __init__(self,gfn,ln):
        self.firstName = gfn
        self.lastName = ln
        
    def displayGname(self):
        print(self.firstName + " " + self.lastName)

class Father(grandFather):
    def __init__(self, gfn, ln,fname):
        super().__init__(gfn, ln)
        self.fname = fname
        
    def displayFName(self):
        print(self.fname + " " + self.lastName)
        
class son(Father):
    def __init__(self, gfn, ln, fname,sname):
        super().__init__(gfn, ln, fname)
        self.sname = sname
        
    def displaySname(self):
        print(self.sname + " " +self.lastName)
        
ajay = son("Ramuji","Jawade","Latari","Ajay")

ajay.displayGname()
ajay.displayFName()
ajay.displaySname()

# Hierarchical Inheritance

class Mother:
    def __init__(self,fn,ln):
        self.firstName = fn
        self.lastName = ln
        
    def displayMname(self):
        print(self.firstName + " " + self.lastName)
        
class Son(Mother):
    def __init__(self, fn, ln,sname):
        super().__init__(fn, ln)
        self.sname = sname
        
    def displaySname(self):
        print(self.sname + " " + self.lastName)
        
class Daughter(Mother):
    def __init__(self, fn, ln,dname):
        super().__init__(fn, ln)
        self.dname = dname
        
    def dipslayDname(self):
        print(self.dname + " " + self.lastName)
        
tony = Son("Surekha","Jawade","Ajay")

tony.displayMname()
tony.displaySname()

seema = Daughter("Surekha","Jawade","Seema")

seema.displayMname()
seema.dipslayDname()

# MULTIPLE INHERITANCE

class Papa:
    def __init__(self,fn,ln):
        print("Papa Class")
        self.firstName = fn
        self.lastName = ln 
        
    def diplayPapaName(self):
        print(self.firstName + " " + self.lastName)
        
class Mom:
    def __init__(self,fn,ln):
        print("Mom Class")
        self.firstName = fn
        self.lastName = ln
        
    def displayMomName(self):
        print(self.firstName + " " + self.lastName)
    
class Potta(Papa,Mom):
    def __init__(self, fn, ln,potta):
        super().__init__(fn, ln)
        self.pottaName = potta
        
    def displayPottaName(self):
        print(self.pottaName + " " + self.lastName)
        
aju = Potta("Latari","Jawade","Aju")


aju.diplayPapaName()
aju.displayMomName()
aju.displayPottaName()    