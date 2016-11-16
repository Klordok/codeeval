#Find a Writer
#https://www.codeeval.com/open_challenges/97/
#Your goal is to go through each number in the key (numbers are separated by space) left-to-right.
#Each number represents a position in the 1st part of a row.

"""
osSE5Gu0Vi8WRq93UvkYZCjaOKeNJfTyH6tzDQbxFm4M1ndXIPh27wBA rLclpg| 3 35 27 62 51 27 46 57 26 10 46 63 57 45 15 43 53

3Kucdq9bfCEgZGF2nwx8UpzQJyHiOm0hoaYP6ST1WM7Nks5XjrR4IltBeDLV vA| 2 26 33 55 34 50 33 61 44 28 46 32 28 30 3 50 34 61 40 7 1 31
"""

test = ''#input
test_cases = ''
author = ''

def decoder(test):
    code = test.split('| ')[0]#letter number sequence
    key = test.split('| ')[1]#number key
    key = key.split()#make key a list
    author = ''

    for number in key:
        author = author + code[int(number)-1]#index is 1 less than 'real' position. Add corresponding letter to author.

    print(author)
    return
    
test = str(input("Enter name/key pair:"))
decoder(test)



    
#Submitted code
"""
import sys

test = ''#input
test_cases = ''
author = ''

def decoder(test):
    code = test.split('| ')[0]#letter number sequence
    key = test.split('| ')[1]#number key
    key = key.split()#make key a list
    author = ''

    for number in key:
        author = author + code[int(number)-1]#index is 1 less than 'real' position. Add corresponding letter to author.

    print(author)
    return

with open(sys.argv[1], 'r') as test_cases:
    for test in test_cases:
        decoder(test)
"""
