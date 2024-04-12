# rb = open("aj.jpg","rb")
# rb2 = open("aj2.jpg","wb")

# bytes = rb.read()
# rb2.write(bytes)

# rb.close()
# rb2.close()

# Program 1

# with open("info4.txt",'w') as f:
#     f.write("Iam Learing JS \n")
#     f.write("Iam Learing PY")
    
# with open("info4.txt","r") as f2:
#     str = f2.read()
#     print(str)
    
# Program 2

# Class - User Define Data Type

import pickle

class emp:
    def __init__(self,fn,ln,age,email):
        self.firstName = fn
        self.lastName = ln
        self.age = age
        self.email = email
        
    def details(self):
        print(self.firstName)
        print(self.lastName)
        print(self.age)
        print(self.email)
    
# f = open("student.dat","wb")
# n = int(input("Enter Number of Object to Create : "))

# for x in range(n):
#     fn = input()
#     ln = input()
#     age = input()
#     email = input()
    
#     obj = emp(fn,ln,age,email)
#     pickle.dump(obj,f)
    
# f.close()

with open("Student.dat","wb") as dat:
    n = int(input("Enter Number Of Elements : "))
    
    for x in range(n):
        fn = input("Enter First Name : ")
        ln = input("Enter Last Name : ")
        age = input("Enter Age : ")
        email = input("Enter Email : ")
        
        obj = emp(fn,ln,age,email)
        pickle.dump(obj,dat)        
        
    
        

    

