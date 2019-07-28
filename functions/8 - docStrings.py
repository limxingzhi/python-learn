def print_max(x,y):
    '''This function prints the max value among the 2 numbers
both input must be integers'''


    x = int(x)
    y = int(y)

    if x > y :
        print(x, 'is max')
    elif y < y:
        print (y, 'is max')
    else:
        print('bruh plz')

print_max(3, 5)
print('the next line is the doc string')
print(print_max.__doc__)
