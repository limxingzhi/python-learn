def foo(param1, param2 = '2not', param3 = '3not'):
    print(param1,param2,param3)

foo('alpha','bleh','cool')

foo('alpha',param3 = 'cooooool')

foo(param2 = 'blows', param1 = 'ah')
