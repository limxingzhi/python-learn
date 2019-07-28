print('===== dictionary is a bunch of key values, they are unordered =====\n')

'''
dictionary works kinda like JSON:

1. the value can be objects
2. BUT the key is immutable but the value isn't

'''


address_book = {
    'justine': 12345,
    'bleh': 54321
}

print('current address book:', address_book)

print('justin\'s number is', address_book['justine'])

# deleting a key value pair

del address_book['bleh']
print('\nafter deleting bleh\n', address_book)

address_book['linustechtips'] = 6969
print('\nafter assigning linustechtips:\n', address_book)

address_book['justine'] = 29126
print('\nafter changing justine\'s number:\n', address_book)
