# from abc import ABC,abstractmethod

# class WorldBank(ABC):
#     @abstractmethod
#     def loan(self,x):
#         pass
#     @abstractmethod
#     def save(self,x):
#         pass
    
# # WE CANNOT CREATE OBJECT OF ABSTRACT CLASS

# # obj = WorldBank()

# class SBI(WorldBank):
#     def loan(self,x):
#         print("loan is " + str(x))
        
#     def save(self,x):
#         print("save is " + str(x))
        
#     def branchName(WorldBank):
#         print("Nagpur")

# class PNB(WorldBank):
#     def loan(self,x):
#         print("loan is " + str(x))
#     def save(self,x):
#         print("save is " + str(x))
    
# nagpur = SBI()

# nagpur.loan(3)
# nagpur.save(5)
# nagpur.branchName()

# nagpurPNB = PNB()

# nagpurPNB.loan(9)
# nagpurPNB.save(7)

from abc import ABC,abstractmethod

class WorldBank(ABC):
    @abstractmethod
    def loan(self):
        pass
    
    @abstractmethod
    def save(self):
        pass
    
    def countrty(self):
        print("Bharat")
    
class SBI(WorldBank):
    
    def loan(self):
        print("Loan From SBI")
        
    def save(self):
        print("Save from SBI")
        
class PNB(WorldBank):
    
    def loan(self):
        print("Loan from PNB")
        
    def save(self):
        print("Save from PNB")
        
sbi = SBI()

sbi.loan()
sbi.save()
sbi.countrty()




