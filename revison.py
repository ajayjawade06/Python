'''x = 10
print(x)

a = 20
b = 4

print(a + b)
print(a - b)
print(a * b)
print(a / b)
print(a % b)

def add ():
    print(2 + 3)

add()
add()   '''

def calculator(a,b):
    print(a + b)
    print(a - b)
    print(a * b)
    print(a / b)
    print(a % b)

calculator(4,2)

def cal(x,y):
    return x+y

q1 = cal(8,2)
print(q1 )
print(q1 + 5)
print(q1 - 5)
print(q1 * 5)


print(9>0  and 9>9)

for x in range(2,21,2):
    print(x)
    
for x in range(50,4,-5):
    print(x)
    
    
str = "AJAYJAWADE"

for num in str:
    print(num)

for x in range(len(str)):
    print(str[x])
    
print(str[0:len(str):3])
print(str[0:len(str) - 1:3])


names = ['ajay','raju','kaju','seema']
names.append('Aju')    
print(names)

names.sort()
print(names)

names.extend(['Shrusti','Priya'])
print(names)

names.insert(2,"bhalu")
print(names)

names.remove('bhalu')
print(names)

names.pop(3)
print(names)

#names.clear()
#print(names)

q1 = names.count('ajay')
print(q1)

names.reverse()
print(names)
