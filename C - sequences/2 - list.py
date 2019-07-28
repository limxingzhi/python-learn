shoplist = ['pen', 'apple', 'pineapple']

print('shoplist has this number of items:', len(shoplist))
print('shop list has these items:', end=' ')
# https://www.geeksforgeeks.org/gfact-50-python-end-parameter-in-print/
# end is a parameter for print. With end, print does not make a new line

for item in shoplist:
    print(item, end=' ')

print('\nadding rice')
shoplist.append('rice')
print('shoplist is:', shoplist)

print('item at the 0th position is', shoplist[0])

del shoplist[2]
print('after removing the 3rd item at position 2, shoplist is', shoplist)
