# Not only that, functions can be passed as argument to another function.

def fxy(f, x, y):
    return f(x) + f(y)

def square(x):
    return x*x

print fxy(square, 3, 4)