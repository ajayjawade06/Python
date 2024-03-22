class WorldBank:
    
    def loan(self):
        print("I am Loan")
        
    def save(self):
        print("I am save")
        
class SBI(WorldBank):
     def loan(self):
        print("I am Loan from SBI")
        
     def save(self):
        print("I am save from SBI")

class PNB(WorldBank):
     def loan(self):
        print("I am Loan from PNB")
        
     def save(self):
        print("I am save from PNB")

nagpur = SBI()


nagpur.loan()
nagpur.save()