#Kelsey Krehbiel
#Beautiful Strings
"""
Given a string s, little Johnny defined the beauty of the string as the sum of the beauty of the letters in it.
The beauty of each letter is an integer between 1 and 26, inclusive, and no two letters have the same beauty.
"""

#ignore punctuation
#count number of each letter
#assign value to letters, highest frquency gets highest value
#add values together
#ABbCcc -> 152

test = 'ABb,?Ccc'

test = test.lower()

alphabet = 'abcdefghijklmnopqrstuvwxyz'

characters = []

for letter in test:
    if letter in alphabet:
        characters += letter

charCounts = {letter: characters.count(letter) for letter in characters}

print(OrderedDict(sorted(charCounts.items(), key=lambda t: t[1])))

#print(charCounts)
    
