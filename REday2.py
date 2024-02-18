import re

# SEARCH

str1 ="an apple a day keeps the doctor away"

e2 = re.findall(r'\ba\w*\b',str1)

print(e2)

str2 = "the class will be conducted on 6AM and 10PM everyday"

e3 = re.findall(r'\d\w*\b',str2)

print(e3)

str3 = "one two three four five six seven 8 9 10"

e4 = re.findall(r'\b\w\w\w\w\w',str3)

print(e4)

e5 = re.findall(r'\b\w{5}',str3)
print(e5)

e6 = re.search(r'\b\w{5}',str3)
print(e6.group())

str4 = "one two three four five six seven nineteen 8 9 10"

e7 = re.findall(r'\b\w{5}',str4)
print(e7)

e8 = re.findall(r'\b\w{5}\b',str4)
print(e8)

e9 = re.findall(r'\b\d{1,}\b',str4)
print(e9)

e10 =re.findall(r'\b\w{3,5}\b',str4)
print(e10)

e11 = re.findall(r'\b\d+\b',str4)
print(e11)

# e12 = re.findall(r'\b\d*\b',str4)
# print(e12)

# '\Z' end of the string
# '\A' start of string

e13 = re.findall(r'\A\bo\w*',str4)
print(e13)


str5 = "one two three four five six seven"
e14 = re.findall(r'\bs\w*\Z',str5)
print(e14)






