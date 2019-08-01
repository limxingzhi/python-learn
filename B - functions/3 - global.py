x = 50

def foo(x):
    # x is now local
    print('local x is',x)
    x = 2
    print('local x is now',x)

foo(x)

print('\n')

def bar():
    global x
    # x is now local
    print('local x is the same as global at',x)
    x = 2
    print('local and global x is now',x)

bar()
print('global value of x is',x)
