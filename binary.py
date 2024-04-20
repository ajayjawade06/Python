# reclen = 20

# with open('cities.bin','wb') as f :
#     n = int(input("Enter the Number of Cities : "))
#     for x in range(n):
#         city = input("Enter City Name : ")
#         city = city + (reclen - len(city)) * " "
#         city = city.encode()
#         f.write(city)
        
# program

reclen = 20

with open('cities.bin','rb') as f :
    n = int(input("Record Number : "))
    f.seek(reclen * (n-1))
    str = f.read(reclen)
    str = str.decode()
    print(str)