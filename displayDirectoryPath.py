#https://www.codementor.io/python/tutorial/essential-python-interview-questions
#Kelsey Krehbiel
#Question 2
import os

def print_directory_contents(sPath):
    print("I'm in the function ")                   
    for sChild in os.listdir(sPath):
#        print(sChild)
        sChildPath = os.path.join(sPath,sChild)
#        print (sChildPath)
        if os.path.isdir(sChildPath):
            print_directory_contents(sChildPath)
        else:
            print(sChildPath)

sPath = str(input("enter the full path of the directory you want to explore. No drive leter, use forward slashes:"))
    

print_directory_contents(sPath)
    

#Answer
"""
def print_directory_contents(sPath):
    import os                                       
    for sChild in os.listdir(sPath):                
        sChildPath = os.path.join(sPath,sChild)
        if os.path.isdir(sChildPath):
            print_directory_contents(sChildPath)
        else:
            print(sChildPath)
"""
