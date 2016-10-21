#Kelsey Krehbiel
#Multiples of a number
#Given numbers x and n, where n is a power of 2,
#print out the smallest multiple of n which is greater than or equal to x.
#Do not use division or modulo operator. 


test = '17,16'

x = int(test.split(sep=',')[0])

n = int(test.split(sep=',')[1])
print('x =', x)

print('n =', n)

multiple = n

print('multiple =', multiple)

while multiple < x:
    multiple = multiple + n
    print(multiple)
    
"""


import sys
test_cases = open(sys.argv[1], 'r')
for test in test_cases:
    x = int(test.split(",")[0])

    n = int(test.split(",")[1])
    
    multiple = n
    
    while multiple < x:
        multiple = multiple + n
    print(multiple)
    # ignore test if it is an empty line
    # 'test' represents the test case, do something with it
    # ...
    # ...

test_cases.close()

"""
