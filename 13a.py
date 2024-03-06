name = "   ajay   "

a1 = name.startswith("A")
print(a1)

a2 = name.replace("A","a")
print(a2)

print("-".join(["chinmay","deshpande","shrish"]))

a3 = name.capitalize()
print(a3)

a3 = name.isalnum()
print(a3)

a3 = name.index("a")
print(a3)

a4 = name.endswith("y")
print(a4)

a5 = name.lstrip()
print(a5)

a6 = name.rstrip()
print(a6)

a7 = name.strip()
print(a7)

a8 = name.isdigit()
print(a8)

a9 = "1029281873".isdigit()
print(a9)

listA = ['Ajay',123,True,12.3,"Ajay"]
print(listA)

a10 = name.title()
print(a10)


full_name = " a"

e3 = full_name.isspace()
print(e3)


name = "ajay"
e4 = name.capitalize()
print(e4)


e5 = "Iam Learning Js"

print(e5.istitle())

info = ["ajay","jawade","7972235361"]
e5 = "@".join(info)
print(e5)

email = "ajayjawade@gmail.com"

e6 = email.split("@")
print(e6)


# Find

email1 = "gmail.com@ajay"
email2 = "gmail.com@raju"
email3 = "gmail.com@aditya"

# print(email3.removeprefix("gmail.com@"))

students = [email1,email2,email3]

lista = []

for x in students:
    q1 = x.removeprefix("gmail.com@")
    lista.append(q1)
    
print(lista)

students = {
    
    "1":"ajayadmin",
    "2":"rajuceo",
    "3":"kajucustomer",
    "4":"adityamanager"
    
}

roles = ["admin","ceo","customer","manager"]
names = []

# for name in students.values():
#     for role in roles:
#      if role in name:
#         q2 = name.removesuffix(role)
#         names.append(q2)
        
# print(names)


q1 = list(map(lambda x:x.removesuffix("admin"),students.values()))
print(q1)


# swapcase()

a = "hello"
print(a.swapcase())

# zfill()

name1 = "ajay"
name2 = "tonyyy"

print(name1.zfill(10))
print(name2.zfill(10))


