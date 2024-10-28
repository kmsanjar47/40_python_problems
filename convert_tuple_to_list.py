# Simple calculator using functions for basic operations.

def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b

def divide(a, b):
    if b != 0:
        return a / b
    return 'Cannot divide by zero'

print('Add:', add(4, 5))
print('Subtract:', subtract(9, 3))
print('Multiply:', multiply(4, 5))
print('Divide:', divide(10, 2))
