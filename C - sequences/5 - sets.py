print('===== sets are unordered =====\n')
# https://docs.python.org/3/library/stdtypes.html#set-types-set-frozenset

asian_countries = set(['singapore','china','hongkong'])
print(asian_countries)

print('\nis singapore in asian_countries?', 'singapore' in asian_countries)
print('is singapore not in asian_countries?', 'singapore' not in asian_countries)

countries = asian_countries.copy()
print('\na copy of asian_countries is', countries)

countries.add('france')
print('\n',countries)
print('after adding france, is countries a superset of asian_countries?'
      ,countries.issuperset(asian_countries))

print('\n',countries)
asian_countries.remove('china')
print('after removing china, where does the 2 sets intersect?\n', asian_countries.intersection(countries))
print('alternative syntax of intersection\n', asian_countries & countries)
