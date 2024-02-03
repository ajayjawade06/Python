def add(x,y):
    return "hello"
q1 = add(23,4)
print(q1)

names = ['ajay','aju','seema','tejas','komal']
q1 = len(names) 
print(q1)
print(names)

e = names.append('achal')   
print(names)
print(e)    

fruits = ['grapes','gauva','banana','banana','mango','tomato']
#fruits.clear()
#print(fruits)

i = fruits.count('banana')
print(i)

names.extend(['surekha','priyanka'])
print(names)

fruits.insert(2,'mango')
print(fruits)

fruits.pop()
print(fruits)

fruits.pop(3)
print(fruits)

names.remove('surekha')
print(names)    

a = names.index("aju")
print(a)

a1 = fruits.copy()
print(fruits)   
print(a1)

print(type(a1))

a1 = [1,2,43,56,78,88]
for c in range(len(a1)):
    print(a1[c])
    
    
 
    
        
    
    
    
    





