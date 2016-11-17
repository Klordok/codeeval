#Kelsey Krehbiel
#Multiplication Tables
#Print out the grade school multiplication table upto 12*12.

for row in range(1,13):
    output = ''
    for column in range(1,13):
        product = str(row*column)

        if row < 10:
            product = ' '+product#add a space so numbers allign with double digits
        if column > 1:
            while len(product) < 4:#total column width is 4 characters
                product = ' '+product#add spaces to make it pretty
                
        output = output+product

    print(output)

#Solved as is
