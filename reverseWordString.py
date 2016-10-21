#kelsey krehbiel
#reverse word order
#Write a program which reverses the words in an input sentence. 

test = 'Hello World'

words = test.split()
reverseWords = ''

words.reverse()

for word in words:
    reverseWords += word
    if words.index(word) < len(words):
        reverseWords += ' '

print(reverseWords)

"""
#kelsey krehbiel
#reverse word order
#Write a program which reverses the words in an input sentence. 

import sys
test_cases = open(sys.argv[1], 'r')
for test in test_cases:
    words = test.split()
    reverseWords = ''
    
    words.reverse()
    
    for word in words:
        reverseWords += word
        if words.index(word) < len(words):
            reverseWords += ' '
    
    print(reverseWords)

test_cases.close()
"""
