def foo(param1, param2 = '2 not assigned', param3 = '3 not assigned'):
    print(param1,'\n',param2,'\n',param3)

foo('alpha','bleh','cool')

foo('alpha',param3 = 'cooooool')

foo(param2 = 'blows', param1 = 'ah')
