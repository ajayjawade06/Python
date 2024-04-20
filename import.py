import pickle

class Emp:
    def __init__(self,fn,ln,sal):
        self.firstname = fn
        self.lastname = ln
        self.salary = sal
        
def displayInfo(self):
    print(self.firstname)
    print(self.lastname)
    print(self.salary)
    
# f = open('emp.dat','wb')
# users = int(input("Enter Number of Users : "))

# for i in range(users):
#     fn = input("Enter First Name : ")
#     ln = input("Enter Last Name :")
#     sal = float(input("Enter Salary : "))
    
# e = Emp(fn,ln,sal)
# pickle.dump(e,f)

f = open('emp.dat',"rb")

while True:
    try:
        e = pickle.load(f)
        e.dipslayInfo()
    except:
        print("EOF FILE REACHED")
        break

f.close()

