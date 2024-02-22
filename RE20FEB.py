
# 20 Feb 2024
import re

str = "Ajay Jawade : 7972235361"

print(str)

e = re.search(r'\d+',str)

print(e.group())

e = re.search(r'\D+',str)
print(e.group())

e = re.search(r'\w+',str)
print(e.group())


e = re.search(r'\w+',str)
print(e.group())

f = re.search(r'[\w]*[\w]*',str)
if f:
    print(f.group())
else:
    print("pattern not found")
    
f = re.search(r'[\w]*[\w]*',str)
if f:
    print(f.group())
else:
    print("pattern not found")

str1 = "ajay arun amit ananya ankur ajey"

q1 = re.findall(r'\ba[nkr][\w]*',str1)
print(q1)

str2 = "ajay 06-07-2003 raju 11-03-2001 tejas 12-05-1990"
q2 = re.findall(r'\d{2}-\d{2}-\d{4}',str2)
print(q2)

str2 = "ajay 06-07-2003 raju 11-03-2001 tejas 12-05-1990"
q2 = re.findall(r'\d+-\d+-\d+',str2)
print(q2)

str2 = "ajay 06-07-2003 raju 11-03-2001 tejas 12-05-1990"
q2 = re.findall(r'\d*-\d*-\d*',str2)
print(q2)

str2 = "ajay 06-07-2003 raju 11-03-2001 tejas 12-05-1990"
q3 = re.findall(r'\d{1,2}-\d{2}-\d{4}',str2)
print(q3)

str4 = "hello ajay"
q4 = re.search(r'^he',str4)
print(q4.group())

str5 = "hello ajay"
q5 = re.search(r'ajay$',str5)
print(q5.group())

str6 = "hello ajay"
q6 = re.search(r'Ajay$',str6,re.IGNORECASE)
print(q6.group())

students = "Ajay got 88 Marks Raju got 90 Marks"
f = re.findall(r'[A-Z][a-z]*',students)
print(f)

str = 'The morning meeting will be schedule at 8am or 9am , evening at 8pm or 9pm'

x1 = re.findall(r'[0-9][\w]*',str)
print(x1)   

for item in x1:
    print(item)
    
