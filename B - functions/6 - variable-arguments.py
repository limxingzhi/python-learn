def total(a = 5, *args, **kwags):
    print('a which is the first parameter:', a,'\n')

    print('single arguments')
    #iterate through all the numbers in tuple
    for single_item in args:
        print(single_item)

    print('\n')

    print('keyword arguments or kwags')
    #iterate through all the times in dictionary
    for first_part, second_part in kwags.items():
        print(first_part, second_part)

total(10,1,1,2,3,Jack=1123, John=2231, Inge=1560)
