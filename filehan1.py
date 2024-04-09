# Creating and Writing Content to File

# w = open("myfile.txt",'w')

# content = input("Enter the File Content : ")

# w.write(content + "\n")

# w.close()

# Reading the Content Of File

# fileName = input("Enter File Name To Open : ")

# r = open(fileName,'r')

# fileToOpen = r.read()
# print(fileToOpen)

# r.close()


w = open("myfile.txt","w")

while str != '@' :
    str = input("Enter the File Content : ")
    if str != '@':
        w.write(str + '\n')
    
w.close()
    
# #########################################################################

r = None

try:
    
    fileName = input("Enter File Name To Open : ")
    r = open(fileName,'r')
    con = r.read()
    print(con)

except FileNotFoundError as e:
    print("File Not Found ",e)
    
finally:
    if r is not None:
        r.close()
print("Hello Ajay")


