#First Non-Repeated Character
#a program which finds the first non-repeated character in a string.
#Kelsey Krehbiel
#https://www.codeeval.com/open_challenges/12/

#submitted code
"""
import sys

with open(sys.argv[1], 'r') as test_cases:
    for test in test_cases:
        for char in range(len(test)-1):
            if test[char] == test[char+1]:#if consecutive characters are the same
                print(test[char])
                break#done with word

test_cases.close()
"""

#output
"""
l
l
f
e
o
e
"""

#test code
test = ""
def nonFinder(test):
    for char in range(len(test)-1):
        if test[char] == test[char+1]:#if consecutive characters aren't the same
            print(test[char])
            break#done with word
    return
            
test  = str(input("String: "))
nonFinder(test)
