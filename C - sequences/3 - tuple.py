print('===== tuple are immutable =====\n')

old_animals = ('camel', 'elephant', 'snakey')
print('number of old animals is', len(old_animals))

new_animals = ('bear', 'shark', 'baby shark dooo dooo' ,old_animals)

print('all animals are', new_animals)

print('old animals are', new_animals[-1])
