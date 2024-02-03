"""def sum(x,y):
    return x + y

c = sum(23,5)
print(c)


def even_odd(n):
    if n % 2 == 0:
        print(n," is even")
    else:
        print(n," is Odd")

even_odd(3)
even_odd(6)
"""


"""def fact(num):
    a = 1
    while(num >= 1):
        a *= num   
        num -= 1         
        
    return a 
        

for i in range(1,11):
    print("Factorial of",i,"is" ,fact(i))
"""    
'''def prime(n):
    x = 1
    for i in range(2,n):
        print(i)
        if  n % i == 0:
            x = 0
            break
        else:
            x = 1
    return x

num = int(input('Enter a Number : '))

result = prime(num)

if result == 1:
    print(num, "is Prime Number.")
else:
    print(num, "is Not Prime Number.")'''
 
"""def prime(n):
    x = 1
    for i in range(2,n):
        if  n % i == 0:
            x = 0
            break
        else:
            x = 1
    return x

num = int(input('How many Prime Number Do you want : '))
i = 2
c = 1

while True:
    if prime(i):
        print(i)
        c +=1
    i +=1
    if c > num:
        break
"""

def sum_sub(a,b):
    c = a+b
    d = a - b
    return c,d

x , y = sum_sub(10,6)
print("Addition is ",x)
print("Substraction is ",y)

def dmasmo(q,r):
    a = q + r
    s = q - r
    m = q * r
    d = q / r
    mo = q % r
    return a,s,m,d,mo

a1,a2,a3,a4,a5 = dmasmo(10,5)
t = dmasmo(9,4)
print("Addition is ",a1)
print("Substraction is ",a2)
print("Multiplication is ",a3)
print("Division is ",a4)
print("Modulas is ",a5)

for i in t:
    print(i,)
    

    
    





 
     




