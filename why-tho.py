import math

x = 1

print('\nLine 5: Original value of x is')
print(x)  # 1


def test_no_assignment():
    print('\nLine 10: No assignment, x is ')
    print(x)


def test_assignment():
    x = 2
    print('\nLine 16: After assignment, x is ')
    print(x)


def print_before_assignment():  # this function is illegal
    print(x)  # UnboundLocalError: local variable 'x' referenced before assignment
    x = 3


test_no_assignment()  # 1
test_assignment()  # 2
# print_before_assignment()


print('\nLine 30: Global value of x after function execution is')
print(x)  # 1
