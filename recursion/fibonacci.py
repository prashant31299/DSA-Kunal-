# Python code to implement Fibonacci series

# Function for fibonacci
def fib(n):
    if n< 2:
        return n
    return fib(n-1)+fib(n-2)
print(fib(6))