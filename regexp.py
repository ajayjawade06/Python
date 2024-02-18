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



