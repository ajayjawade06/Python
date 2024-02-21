# SEARCH 

import re
str1='cat mat sat dat vat chat '

e1 = re.search(r's\w\w',str1)
print(e1.group())

e2 = re.search(r'\wat',str1)
print(e2.group())

if e1:
    print(e1.group())
else:
    print("Match not Found!")
    
if e2:
    print(e2.group())
else:
    print("Match not Found!")
    
    
# FIND ALL

str2 = "man van can san dan cha fat cat sat"

e3 = re.findall(r'c\w\w',str2)
print(e3)

e4 = re.findall(r'\wan',str2)
print(e4)

e5 = re.findall(r'\wat',str2)
print(e5)

# Match

str3 = "mon tue wed thru fri sat"

e6 = re.match(r't\w\w',str3)

if e6:
    print(e6.group())
else:
    print('Match not found')
    
str4 = "this is; the 'school' of IT"

e7 = re.split(r'\W+',str4)

print(e7)

info = "Ajay : 7972235361"
e8 = re.split(r'\W+',info)
print(e8)

# Substitute

str5 ="Iam a teacher at minSkole"

e9 =re.sub(r'teacher','student',str5)
print(e9)

str6 ="one two three four five six seven 8 9 10"
e4 = re.findall(r'\b\w\w\w\w\w',str6)

print(e4)

e5 = re.search(r'\b\w{5}',str6)
print(e5.group())

e6 = re.findall(r'\b\w{5}',str6)
print(e6)

e7 = re.findall(r'\b\w{4,}',str6)
print(e7)

str7 = "one two three four five six seven nineteen 8 9 10"

e8 = re.findall(r'\b\w{3,5}',str7)
print(e8)

e9 = re.findall(r'\b\d{1,}\b',str7)
print(e9)

e10 = re.findall(r'\b\d+\b',str7)
print(e10)


str8 = "one two three four five six seven seventeen"

q1 = re.findall(r'\bs[\w]*\Z',str8)
q2 = re.findall(r'\A\bo[\w]*',str8)

print(q1)
print(q2)



