#https://www.codeeval.com/open_challenges/13/
#Remove Characters
#Write a program which removes specific characters from a string.
#Kelsey Krehbiel


def charScrubber(test):
    sentence, scrub = test.split(', ')#split the string
##    print(sentence)
##    print(scrub)
    for char in sentence:
        if char in scrub:
            sentence = sentence.replace(char, '')
    print(sentence)
    return
            
    

while True:
    test = str(input("String? "))
    if test == "exit":
        break
    charScrubber(test)

#submitted code, Solved
"""

import sys

with open(sys.argv[1], 'r') as test_cases:
    for test in test_cases:
        sentence, scrub = test.split(', ')#split the string
        ##    print(sentence)
        ##    print(scrub)
        for char in sentence:
            if char in scrub:
                sentence = sentence.replace(char, '')
        print(sentence)
        
test_cases.close()
"""
