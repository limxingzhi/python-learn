x = 50

def foo():  
    print('x is',x)
    x = 2
    print('global x is now',x)

foo()
print('value of x is',x)
