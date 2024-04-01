# a = 100                                                                     
# b = 200                                                                     
# c = 0                                                                       
#                                                                             
# print(a/b)                                                                  
# print(a/c)                                                                  
#                                                                             
# print("Hello World!")                                                       
                                                                              
# name = "Snehal"                                                             
#                                                                             
# print(name)                                                                 
#                                                                             
# print(name[0])                                                              
# print(name[6])                                                              
                                                                              
# a = 100                                                                     
# b = "One"                                                                   
# print(a+b)                                                                  
                                                                              
# a = 100                                                                     
#                                                                             
# try :                                                                       
#      b = 0                                                                  
#      c = a/b                                                                
#      print(c)                                                               
#                                                                             
# except:                                                                     
#     print("Some Error Occured!")                                            
#                                                                             
# print("Hello Snehal!")                                                      
#                                                                             
# name = "Snehal"                                                             
#                                                                             
# try :                                                                       
#     print(name[0])                                                          
# except :                                                                    
#     print("Something went wrong!")                                          
#                                                                             
# try :                                                                       
#     print(name[6])                                                          
# except :                                                                    
#     print("Something went wrong!")                                          
                                                                              
# a = 100                                                                     
# name = "Snehal"                                                             
#                                                                             
# try :                                                                       
#     b = 0                                                                   
#     c = a/b                                                                 
#     print(c)                                                                
#     print(name[10])                                                         
#                                                                             
# except Exception as d:                                                      
#     print("Some error Occurred",d)                                          
#                                                                             
# except Exception as s:                                                      
#     print("Some error Occured!",s)                                          
#                                                                             
# print("Hello Snehal")                                                       
#                                                                             
# try :                                                                       
#     b = 2                                                                   
#     c = a/b                                                                 
#     print(c)                                                                
#     print(name[10])                                                         
#                                                                             
# except ZeroDivisionError as d:                                              
#     print("Some error Occurred",d)                                          
#                                                                             
# except IndexError as e:                                                     
#     print("Some error Occurred",e)                                          
#                                                                             
                                                                              
a =100                                                                        
                                                                              
name = "Ajay"                                                                 
                                                                              
try :                                                                         
    b = 100                                                                   
    c = a/b                                                                   
    print(c)                                                                  
    print(name[5])                                                            
                                                                              
except ZeroDivisionError as e:                                                
    print(e)                                                                  
                                                                              
except IndexError as f :                                                      
    print(f)                                                                  
                                                                              
else:                                                                         
    print("Code Executed Succesfully!")                                       
                                                                              
finally:                                                                      
    print("This will always get Executed , irrespective of the code status!")