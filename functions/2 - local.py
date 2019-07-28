x = 50

def foo_bar(x):
    print('x before assigning in scope is',x)
    x = 2
    print('x after assigning in scope is',x)

foo_bar(x)
print('x in the global scope is still', x)
