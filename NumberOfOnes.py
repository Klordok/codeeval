#Kelsey Krehbiel
#Number of Ones
#https://www.codeeval.com/open_challenges/16/
#Write a program which determines the number of
#1 bits in the internal representation of a given integer.

test = ''

def numberOne(test):
    binary = format(int(test),'b')#convert to int, get binary
    ones = 0
    for digit in binary:
        if digit == '1':
            ones += 1
    return ones

test = input("number:")
print(numberOne(test))


#Submitted
"""

import sys

def numberOne(test):
    binary = format(int(test),'b')#convert to int, get binary
    ones = 0
    for digit in binary:
        if digit == '1':
            ones += 1
    return ones
    
with open(sys.argv[1], 'r') as test_cases:
    for test in test_cases:
        print(numberOne(test))

"""
