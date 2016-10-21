#kelsey krehbiel
#unique elements
#You are given a sorted list of numbers with duplicates.
#Print out the sorted list with duplicates removed.

test = '1,1,2,10,10,10,10,11,12,13,13,14,15,16,17,17\n'

if '\n' in test:
    test = test[0:-1]
uniqueElements = ''

testList = test.split(',')
# call int(x) on each element before comparing it
testList = [int(item) for item in testList]

print(testList)

filteredList = set(testList)

print("".join(filteredList))




print(uniqueElements)
    
