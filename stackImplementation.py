#Stack Implementation
#https://www.codeeval.com/open_challenges/9/
#Write a program which implements a stack interface for integers.
#The interface should have ‘push’ and ‘pop’ functions.
#Your task is to ‘push’ a series of integers and then ‘pop’ and print every alternate integer. 

def altPop(test):
    popped = ""#output
    intList = test.split()#put the ints in a list
    index = len(intList)
    while index >= 1:
        popped += intList.pop(index-1)+" "#count from end of list. add to popped string
        index -= 2
    print(popped)
        

while True:
    test = str(input("numbers? "))
    if test == 'exit':
        break
    altPop(test)

#submitted code, Solved
"""
import sys

with open(sys.argv[1], 'r') as test_cases:
    for test in test_cases:
        popped = ""#output
        intList = test.split()#put the ints in a list
        index = len(intList)
        while index >= 1:
            popped += intList.pop(index-1)+" "#count from end of list. add to popped string
            index -= 2
        print(popped)
        
test_cases.close()
"""
