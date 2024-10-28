# Using recursion to find the nth Fibonacci number.

def fibonacci(n):
    if n <= 1:
        return n
    return fibonacci(n - 1) + fibonacci(n - 2)

n = 5
result = fibonacci(n)

print(f"Fibonacci({n}):", result)
