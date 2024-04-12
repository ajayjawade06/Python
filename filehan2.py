
# f = None

# try:
#     fileName = input("Enter File Name : ")
#     f = open(fileName,"r")
#     read = f.read()
#     print(read)
    
# except FileNotFoundError :
#     print("File Not Found ")
    
# finally:
#     if f is not None:
#         f.close()
        
# fileName = input("Enter File Name : ")

# f  =  open(fileName,"w")

# while str != '@':
#     str = input("Enter Name : ")
   
#     if str != "@":
#         f.write(str + "\n")

# f = open(fileName,"r")
# str = f.read()
# print(str)
# f.close()


# Program  "a+"

# filename = input("Enter File Name : ")

# f = open(filename,"a+")

# while str != '@':
#     str = input("Enter Name : ")
#     if str != '@':
#         f.write(str + "\n")

# str = f.read() // End of File
# print(str)
    
# f.close()

# filename = input("Enter File Name : ")

# f = open(filename,"a+")

# while str != '@':
#     str = input("Enter Name : ")
#     if str != '@':
#         f.write(str + "\n")

# f.seek(0,0)
# str = f.read() 
# print(str)
    
# f.close()

# Program OS , SYS

import os,sys

# fname = input("Enter File Name : ")

# f = open(fname,'r')

# if os.path.isfile(fname):
#     f = open(fname,'r')
# else:
#     sys.exit()
    
# print("File Contents are : ")

# str = f.read()
# print(str)

# f.close()

# Count Line Words Characters


fname = input("Enter File Name : ")

# f = open(fname,'a+')

# while str != "@":
#     str = input("Enter File Content : ")
#     if str != "@":
#         f.write(str + "\n")

# f = open(fname,"r")

if os.path.isfile(fname):
    f = open(fname,"r")
    str = f.read()
    print(str)
else:
    print("File Not Found")
    sys.exit()

f = open(fname,'r')

lineCount = 0
wordCount = 0
charCount = 0

for line in f:
    lineCount = lineCount + 1
    list = line.split() 
    wordCount = wordCount + len(list)
    charCount = charCount + len(line)
    
print(lineCount)
print(wordCount)
print(charCount)

f.close()







