class A:
    def add(self):
        print("A is Called.") #3
        super().add()
        
class B:
    def add(self):
        print("B is Called.")#5
        super().add()
        
class C:
    def add(self):
        print("C is Called.")#6
        
class X(A,B):
    def add(self):
        print("X is Called") #2
        super().add()
        
class Y(B,C):
    def add(self):
        print("Y is Called.") #4
        super().add() 
        
class L(X,Y,C):
    def add(self):
        print("Z is Called.") #1
        super().add()
        
   
l = L()  
l.add()   