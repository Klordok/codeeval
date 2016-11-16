#Longest Word
#Kelsey Krehbiel
#In this challenge you need to find the longest word in a sentence.
#https://www.codeeval.com/open_challenges/111/

test = ''

def longFinder(test):
    test = test.split()
    longest = ''
    for word in test:
        if len(word) > len(longest):
            longest = word
    return longest

test = str(input("words words words:"))
print(longFinder(test))


#Submitted
"""
import sys

def longFinder(test):
    test = test.split()
    longest = ''
    for word in test:
        if len(word) > len(longest):
            longest = word
    return longest

with open(sys.argv[1], 'r') as test_cases:
    for test in test_cases:
        print(longFinder(test))
"""
