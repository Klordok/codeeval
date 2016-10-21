#Capitalize Words
#Write a program which capitalizes the first letter of each word in a sentence.
#Kelsey Krehbiel
#https://www.codeeval.com/open_challenges/93/

def wordCapper(test):
    wordList = test.split()
    #print(wordList)
    capped = ""
    for word in wordList:
        capped += word.replace(word[0], word[0].upper(), 1)+" "#capitalize first char of words, add to string
    print(capped)

while True:
    test = str(input("string? "))
    wordCapper(test)
 
    
#Submitted code, Works
"""

import sys

with open(sys.argv[1], 'r') as test_cases:
    for test in test_cases:
            wordList = test.split()
            #print(wordList)
            capped = ""
            for word in wordList:
                capped += word.replace(word[0], word[0].upper(), 1)+" "#capitalize first char of words, add to string
            print(capped)
            
test_cases.close()
"""
