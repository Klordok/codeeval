#kelsey krehbiel
#Fizz Buzz

testCase = '2 7 15'

outString = ''

x = 0
y = 0
countTo = 1

parameters = testCase.split()

x = int(parameters[0])
y = int(parameters[1])
countTo = int(parameters[2])

for num in range(1, countTo+1):
    FB = str(num)
    #test if divisible by x
    if num%x == 0:
        FB = 'F'
        #if it is, test for y
        if num%y == 0:
            FB = 'FB'
    #test if divisible by y
    elif num%y == 0:
        FB = 'B'
    
    #add the FB value to the output
    outString = outString + FB
    #if it's not the end of the list add a space
    if num != countTo:
        outString += ' '

print(outString)
        
"""

import sys
test_cases = open(sys.argv[1], 'r')
for test in test_cases:
    outString = ''

    x = 0
    y = 0
    countTo = 1

    parameters = test.split()

    x = int(parameters[0])
    y = int(parameters[1])
    countTo = int(parameters[2])

    for num in range(1, countTo+1):
        FB = str(num)
        #test if divisible by x
        if num%x == 0:
            FB = 'F'
            #if it is, test for y
            if num%y == 0:
                FB = 'FB'
        #test if divisible by y
        elif num%y == 0:
            FB = 'B'
        
        #add the FB value to the output
        outString = outString + FB
        #if it's not the end of the list add a space
        if num != countTo:
            outString += ' '
    
    print(outString)

    # ignore test if it is an empty line
    # 'test' represents the test case, do something with it
    # ...
    # ...

test_cases.close()
"""
