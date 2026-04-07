# functions

# function definition
def add(x, y):
    return x + y


# function call
print(add(10, 20))

# function with parameters
def subtract(x, y):
    return x - y

print(subtract(10, 20))


def multiply(x, y):
    return x * y

print(multiply(10, 20))

def divide(x, y):
    return x / y

print(divide(10, 20))

def remainder(x, y):
    return x % y

print(remainder(10, 20))

def power(x, y):
    return x ** y

print(power(10, 20))

# default arguments
def add(x, y=10):
    return x + y

print(add(10))
print(add(10, 20))

# keyword arguments
def add(x, y=10, z=20):
    return x + y + z

print(add(10, z=20))
print(add(10, 20, z=30))

# variable number of arguments
def add(*args):
    total = 0
    for arg in args:
        total += arg
    return total

print(add(10, 20, 30, 40))
print(add(10, 20, 30, 40, 50, 60))

# keyword arguments
def add(**kwargs):
    total = 0
    for key, value in kwargs.items():
        total += value
    return total

print(add(x=10, y=20, z=30))
print(add(x=10, y=20, z=30, a=40, b=50))

